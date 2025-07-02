# 10-K Token Estimator

This script demonstrates the context length challenges discussed in the "LLMs for Financial Valuation and Analysis" lecture by:

1. Downloading a company's latest 10-K filing from the SEC EDGAR database
2. Estimating the number of tokens required for LLM processing
3. Calculating how many chunks would be needed for different LLM models
4. Showing which models can process the document directly

## Requirements

To run this script, you need the following Python packages:
```
pip install requests beautifulsoup4 tiktoken
```

## Usage

### Basic Usage

Simply run the script:
```
python token_estimator.py
```

By default, it will analyze the 10-K filings for AAPL, TSLA, and MSFT.

### Command-Line Arguments

The script supports several command-line arguments for customization:

```
python token_estimator.py --tickers AAPL GOOG META --save-csv --output my_results
```

Available options:
- `--tickers` or `-t`: List of stock tickers to analyze (e.g., `--tickers AAPL GOOG META`)
- `--output` or `-o`: Directory to save results (default: `results`)
- `--save-csv` or `-s`: Save results to a CSV file
- `--verbose` or `-v`: Print detailed output, including full error tracebacks

### Example for Classroom

```
python token_estimator.py --tickers AAPL TSLA MSFT GOOG META AMZN --save-csv
```

This will analyze 10-K filings for six major tech companies and save the results to a CSV file.

## Output Example

```
============================================================
🔍 10-K TOKEN ANALYSIS FOR AAPL 🔍
============================================================
📅 Filing Date: 2023-11-03
🔑 CIK: 0000320193
🌐 URL: https://www.sec.gov/Archives/edgar/data/320193/000032019323000077/0000320193-23-000077.txt

📊 Document Statistics:
  📝 Characters: 1,245,782
  🔤 Words: 189,372
  🧮 Estimated Tokens: 279,650

✅ Can Process Directly (without chunking):
  GPT-3           : ✗ NO
  GPT-3.5-turbo   : ✗ NO
  GPT-4           : ✗ NO
  GPT-4-32k       : ✗ NO
  Claude-1        : ✗ NO
  Claude-2        : ✓ YES
  Claude-3        : ✓ YES
  Gemini Pro      : ✗ NO
  Gemini 1.5 Pro  : ✓ YES

🧩 Chunks Needed for Full Document:
  GPT-3           : 69 chunks
  GPT-3.5-turbo   : 69 chunks
  GPT-4           : 35 chunks
  GPT-4-32k       : 9 chunks
  Claude-1        : 32 chunks
  Gemini Pro      : 9 chunks

💡 Educational Context:
  This document exceeds most LLMs' context windows, requiring chunking strategies.
```

## Educational Context

This script highlights:

1. **Context Length Challenges**: 10-K filings often exceed the token limits of most LLMs
2. **Need for Chunking**: Most documents require splitting into multiple chunks for processing
3. **Model Selection Impact**: Newer models with larger context windows can process more text at once
4. **Practical Considerations**: When building LLM applications for financial documents, context length is a critical constraint

The example output clearly demonstrates why techniques like chunking are necessary for processing large financial documents, especially with models that have smaller context windows.

## CSV Output

When using the `--save-csv` option, the script generates a CSV file with the following information for each analyzed company:
- Ticker symbol and CIK
- Filing date
- Document statistics (characters, words, tokens)
- Which models can process the document directly
- Number of chunks needed for each model

This data can be imported into Excel or other data analysis tools for further study or visualization.

## Error Handling

The script includes robust error handling for common issues:
- SEC API rate limits and temporary unavailability
- Network connectivity problems
- Missing or malformed 10-K filings

If analysis fails for a particular company, the script will continue with the next one, providing informative error messages.
