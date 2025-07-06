"""
10‑K Token Estimator – HF Tokenizer Edition
==========================================

* Downloads the latest 10‑K filing for a list of companies
* Estimates the token, word and character counts **using any Hugging Face    def _pr    def _pre    def _pretty_print(self, res: Dict) -> None:
        print(
            f"  • Size ≈ {res['text_stats']['estimated_tokens']:,} tokens / "
            f"{res['text_stats']['words']:,} words"
        )
        print(f"  • 10-K URL: {res['filing_url']}")
        fits = {m: ok for m, ok in res["can_process_directly"].items() if ok}
        if fits:
            print("  • Fits whole in: " + ", ".join(fits))
        else:
            smallest = min(self.context_limits, key=self.context_limits.get)
            need = res["chunks_needed"][smallest]
            print(f"  • Needs at least {need} chunks for smallest context model")lf, res: Dict) -> None:
        print(
            f"  • Size ≈ {res['text_stats']['estimated_tokens']:,} tokens / "
            f"{res['text_stats']['words']:,} words"
        )
        print(f"  • Filing URL: {res['filing_url']}")
        fits = {m: ok for m, ok in res["can_process_directly"].items() if ok}
        if fits:
            print("  • Fits whole in: " + ", ".join(fits))
        else:
            smallest = min(self.context_limits, key=self.context_limits.get)
            need = res["chunks_needed"][smallest]
            print(f"  • Needs at least {need} chunks for smallest context model")elf, res: Dict) -> None:
        print(
            f"  • Size ≈ {res['text_stats']['estimated_tokens']:,} tokens / "
            f"{res['text_stats']['words']:,} words"
        )
        print(f"  • 10-K URL: {res['filing_url']}")
        fits = {m: ok for m, ok in res["can_process_directly"].items() if ok}
        if fits:
            print("  • Fits whole in: " + ", ".join(fits))
        else:
            smallest = min(self.context_limits, key=self.context_limits.get)
            need = res["chunks_needed"][smallest]
            print(f"  • Needs at least {need} chunks for smallest context model")rmers` tokenizer** for much greater fidelity than rough heuristics
* Reports whether the whole document fits inside popular LLM context windows
* Optional CSV export keeps the spreadsheet workflow untouched

New in this edition
-------------------
* **`--hf-model` flag** – pass any model name available on the HF Hub, e.g.
  `--hf-model gpt2` (default) or `--hf-model meta-llama/Meta-Llama-3-8B`
* **Streaming token count** – avoids running out of RAM when a filing is huge by
  tokenising in 20 k‑character chunks
* **No tiktoken dependency** – everything now runs off `transformers` only
* **Backward‑compatible CSV schema** – nothing breaks if you relied on the old
  column order

Install the extra requirement:
```bash
pip install transformers>=4.40.0 sentencepiece
```
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional, Tuple

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from transformers import AutoTokenizer
from urllib3.util.retry import Retry

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #

CONTACT_EMAIL = os.getenv("SEC_CONTACT_EMAIL", "jfimbett@gmail.com")
DEFAULT_UA = f"10KTokenEstimator/2.0 (+{CONTACT_EMAIL})"

SEC_TICKER_JSON = "https://www.sec.gov/files/company_tickers.json"
SEC_CIK_SUBMISSIONS = "https://data.sec.gov/submissions/CIK{cik}.json"
SEC_TXT_ARCHIVE = (
    "https://www.sec.gov/Archives/edgar/data/{cik}/{acc_no}/{acc_orig}.txt"
)

# The SEC asks for < 10 requests / second on a single IP. We stay well under.
SEC_POLITE_DELAY = 0.2  # seconds


def _make_session(user_agent: str = DEFAULT_UA) -> requests.Session:
    """Return a `requests.Session` pre‑configured with retries and headers."""
    retries = Retry(
        total=5,
        backoff_factor=1,  # exponential: 1 s, 2 s, 4 s, …
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("GET", "HEAD"),
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retries)
    sess = requests.Session()
    sess.headers.update(
        {
            "User-Agent": user_agent,
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": "application/json, text/plain, */*",
            "Connection": "keep-alive",
        }
    )
    sess.mount("https://", adapter)
    sess.mount("http://", adapter)
    return sess


@dataclass
class TokenEstimator:
    """Analyse a company’s latest 10‑K filing using a HF tokenizer."""

    model_name: str = "gpt2"
    session: requests.Session = field(default_factory=_make_session)
    output_dir: Optional[str] = None

    context_limits: Dict[str, int] = field(
        default_factory=lambda: {
            "GPT‑3": 4096,
            "GPT‑3.5‑turbo": 4096,
            "GPT‑4": 8192,
            "GPT‑4‑32k": 32768,
            "Claude‑1": 9000,
            "Claude‑2": 100000,
            "Claude‑3": 200000,
            "Gemini Pro": 32768,
            "Gemini 1.5 Pro": 1000000,
        }
    )
    _ticker_cache: Dict[str, str] = field(default_factory=dict, init=False, repr=False)
    _tokenizer: AutoTokenizer = field(init=False, repr=False)

    # --------------------------------------------------------------------- #
    # Initialisation
    # --------------------------------------------------------------------- #

    def __post_init__(self) -> None:
        print(f"🔧 Loading HF tokenizer: {self.model_name}")
        self._tokenizer = AutoTokenizer.from_pretrained(self.model_name)

    # --------------------------------------------------------------------- #
    # Public API
    # --------------------------------------------------------------------- #

    def analyse(self, ticker: str) -> Optional[Dict]:
        """End‑to‑end analysis pipeline for a single ticker symbol."""
        print(f"\n🚀 Analysing {ticker.upper()}…")

        cik = self._get_cik(ticker)
        if not cik:
            print(f"❌ CIK not found for {ticker}")
            return None

        filing_url, filing_date = self._get_latest_10k(cik)
        if not filing_url:
            print(f"❌ No 10‑K found for CIK {cik}")
            return None

        print(f"  • Latest 10‑K date {filing_date}")
        text = self._download_text(filing_url)
        if not text:
            print("❌ Could not download filing text")
            return None

        token_stats = self._estimate_tokens(text)
        chunks = self._calculate_chunks(token_stats["estimated_tokens"])

        results = {
            "ticker": ticker.upper(),
            "cik": cik,
            "filing_date": filing_date,
            "filing_url": filing_url,
            "text_stats": token_stats,
            "chunks_needed": chunks,
            "can_process_directly": {
                m: token_stats["estimated_tokens"] <= lim
                for m, lim in self.context_limits.items()
            },
        }
        self._pretty_print(results)
        time.sleep(SEC_POLITE_DELAY)
        return results

    # --------------------------------------------------------------------- #
    # Network helpers
    # --------------------------------------------------------------------- #

    def _get_json(self, url: str) -> dict:
        resp = self.session.get(url, timeout=15)
        resp.raise_for_status()
        time.sleep(SEC_POLITE_DELAY)
        return resp.json()

    def _get_cik(self, ticker: str) -> Optional[str]:
        up = ticker.upper()
        if up in self._ticker_cache:
            return self._ticker_cache[up]
        data = self._get_json(SEC_TICKER_JSON)
        for entry in data.values():
            if entry["ticker"].upper() == up:
                cik = f"{entry['cik_str']:010d}"
                self._ticker_cache[up] = cik
                return cik
        return None

    def _get_latest_10k(self, cik: str) -> Tuple[Optional[str], Optional[str]]:
        data = self._get_json(SEC_CIK_SUBMISSIONS.format(cik=cik))
        recent = data.get("filings", {}).get("recent", {})
        for form, acc_no, date in zip(
            recent.get("form", []),
            recent.get("accessionNumber", []),
            recent.get("filingDate", []),
        ):
            if form == "10-K":
                clean = acc_no.replace("-", "")
                url = SEC_TXT_ARCHIVE.format(cik=cik, acc_no=clean, acc_orig=acc_no)
                return url, date
        return None, None

    def _download_text(self, url: str) -> Optional[str]:
        resp = self.session.get(url, timeout=30)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        text = " ".join(soup.stripped_strings)
        if len(text) < 1_000:
            print("⚠️ Downloaded text is very short – may not be a valid filing")
        return text

    # --------------------------------------------------------------------- #
    # Local processing helpers
    # --------------------------------------------------------------------- #

    def _estimate_tokens(self, text: str, chunk_chars: int = 20_000) -> Dict[str, int]:
        """Return counts – tokenised in manageable chunks to avoid OOM."""
        tok_count = 0
        for start in range(0, len(text), chunk_chars):
            piece = text[start : start + chunk_chars]
            tok_count += len(
                self._tokenizer.encode(piece, add_special_tokens=False, truncation=False)
            )
        return {
            "characters": len(text),
            "words": len(text.split()),
            "estimated_tokens": tok_count,
        }

    def _calculate_chunks(self, tokens: int) -> Dict[str, int]:
        return {m: -(-tokens // lim) for m, lim in self.context_limits.items()}

    # --------------------------------------------------------------------- #
    # Output helpers
    # --------------------------------------------------------------------- #

    def _pretty_print(self, res: Dict) -> None:
        print(
            f"  • Size ≈ {res['text_stats']['estimated_tokens']:,} tokens / "
            f"{res['text_stats']['words']:,} words"
        )
        fits = {m: ok for m, ok in res["can_process_directly"].items() if ok}
        if fits:
            print("  • Fits whole in: " + ", ".join(fits))
        else:
            smallest = min(self.context_limits, key=self.context_limits.get)
            need = res["chunks_needed"][smallest]
            print(f"  • Needs at least {need} chunks for smallest context model")

    # --------------------------------------------------------------------- #
    # CSV utilities – unchanged apart from new default header order
    # --------------------------------------------------------------------- #

    def save_csv(self, results: List[Dict], filename: Optional[str] = None) -> str | None:
        if not results:
            print("No results to save")
            return None
        if not filename:
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"10k_token_analysis_{ts}.csv"
        path = os.path.join(self.output_dir or ".", filename)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            header = (
                ["ticker", "cik", "filing_date"]
                + [f"text_{k}" for k in ("characters", "words", "estimated_tokens")]
                + [f"chunks_{m}" for m in self.context_limits]
            )
            w.writerow(header)
            for r in results:
                w.writerow(
                    [
                        r["ticker"],
                        r["cik"],
                        r["filing_date"],
                        r["text_stats"]["characters"],
                        r["text_stats"]["words"],
                        r["text_stats"]["estimated_tokens"],
                        *[r["chunks_needed"][m] for m in self.context_limits],
                    ]
                )
        print(f"📁 Saved CSV to {path}")
        return path


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Estimate token counts of 10‑K filings for given tickers",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("tickers", nargs="+", help="Ticker symbols", default=["AAPL", "MSFT"])
    p.add_argument("--hf-model", default="gpt2", help="Hugging Face model name for tokeniser")
    p.add_argument("--csv", action="store_true", help="Save results to CSV")
    p.add_argument("--out", default="results", help="Output directory for CSV")
    return p.parse_args()


def main() -> None:
    if sys.version_info < (3, 8):
        sys.exit("Python 3.8 or newer required")
    args = _parse_args()
    est = TokenEstimator(model_name=args.hf_model, output_dir=args.out)
    results = []
    for tkr in args.tickers:
        try:
            res = est.analyse(tkr)
            if res:
                results.append(res)
        except Exception as exc:
            print(f"❗ Error analysing {tkr}: {exc}")
    if args.csv and results:
        est.save_csv(results)


if __name__ == "__main__":
    main()
