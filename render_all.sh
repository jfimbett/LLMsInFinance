#!/bin/zsh
# Script to render all Quarto presentations in the LLMs in Finance course

# Change to the project root directory
cd "$(dirname "$0")"

echo "Rendering all presentations..."

# Render all day lecture presentations
for dir in src/day*/lecture; do
  echo "Rendering $dir/index.qmd..."
  (cd "$dir" && quarto render index.qmd)
done

# Render all day practical session presentations
for dir in src/day*/practical-session; do
  if [ -f "$dir/index.qmd" ]; then
    echo "Rendering $dir/index.qmd..."
    (cd "$dir" && quarto render index.qmd)
  fi
done

# Render preliminaries
if [ -f "src/preliminaries/index.qmd" ]; then
  echo "Rendering src/preliminaries/index.qmd..."
  (cd "src/preliminaries" && quarto render index.qmd)
fi

# Render main index if it exists
if [ -f "index.qmd" ]; then
  echo "Rendering main index.qmd..."
  quarto render index.qmd
fi

echo "All presentations have been rendered successfully!"
