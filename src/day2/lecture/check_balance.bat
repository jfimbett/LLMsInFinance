@echo off
echo Checking for LaTeX notation issues...
findstr /S /R /M /C:"\\text\{[^}]*_[^}]*\}" c:\Users\jfimb\Dropbox\Teaching\LLM\LLMsInFinance\src\day2\lecture\*.qmd

echo.
echo Checking for column blocks...
for %%f in (c:\Users\jfimb\Dropbox\Teaching\LLM\LLMsInFinance\src\day2\lecture\*.qmd) do (
    echo Checking %%f
    findstr /C:":::: {.columns}" /C:"::::" %%f | find /C "::::"
)

echo.
echo Done checking. Review the output to ensure each file has matching opening and closing column tags.
pause
