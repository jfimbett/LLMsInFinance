@echo off
REM Script to help identify and fix remaining column layouts in Quarto files

echo Searching for column layouts in day2 lecture files...
echo.

echo === Files with column layouts ===
findstr /n ":::: {.columns}" "c:\Users\jfimb\Dropbox\Teaching\LLM\LLMsInFinance\src\day2\lecture\*.qmd"

echo.
echo === Files with column definitions ===
findstr /n "::: {.column" "c:\Users\jfimb\Dropbox\Teaching\LLM\LLMsInFinance\src\day2\lecture\*.qmd"

echo.
echo === Checking for any remaining LaTeX underscore issues ===
findstr /r "\\text{.*_.*}" "c:\Users\jfimb\Dropbox\Teaching\LLM\LLMsInFinance\src\day2\lecture\*.qmd"

echo.
echo === Summary ===
echo The above results show what still needs to be fixed manually.
echo Priority: Remove :::: {.columns} and ::: {.column} blocks, merge content into single-column layout.

pause
