#!/usr/bin/env bash
# ------------------------------------------------------------
#  Render a Quarto file and live-reload it in Firefox
# ------------------------------------------------------------
#  Requirements
#    • Quarto  (https://quarto.org)
#    • entr    – file-watcher (`brew install entr` on macOS,
#                                 sudo apt-get install entr   on Linux)
#
#  Usage
#    ./render_and_reload.sh            # watches index.qmd
#    ./render_and_reload.sh slides.qmd # watches another file
#
#  Hint:   chmod +x render_and_reload.sh   (make it executable)
# ------------------------------------------------------------

FILE=${1:-index.qmd}               # default = index.qmd
HTML="${FILE%.qmd}.html"
URL="file://${PWD}/${HTML}"

# ── first build & open the page ──────────────────────────────
quarto render "$FILE"              || exit 1
open -a "Firefox" "$URL"           # macOS; use xdg-open on Linux

# ── watch the .qmd for changes and repeat ───────────────────
echo "$FILE" | entr -r bash -c '
  quarto render "'"$FILE"'" &&                 # rebuild
  sleep 0.2 &&                                 # tiny disk settle
  osascript <<EOF                              # hit ⌘R in Firefox
tell application "Firefox" to activate
tell application "System Events"
  keystroke "r" using {command down}
end tell
EOF
'
