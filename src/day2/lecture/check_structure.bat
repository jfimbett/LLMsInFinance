@echo off
echo Checking structure of all .qmd files in day2/lecture...

echo.
echo Checking 02-how-are-llms-trained.qmd...
findstr /C:":::: {.columns}" /C:"::::" "c:\Users\jfimb\Dropbox\Teaching\LLM\LLMsInFinance\src\day2\lecture\02-how-are-llms-trained.qmd" | find /C "::::"

echo.
echo Checking 03-zero-one-multiple-shot-prompts.qmd...
findstr /C:":::: {.columns}" /C:"::::" "c:\Users\jfimb\Dropbox\Teaching\LLM\LLMsInFinance\src\day2\lecture\03-zero-one-multiple-shot-prompts.qmd" | find /C "::::"

echo.
echo Checking 04-tracing-thoughts.qmd...
findstr /C:":::: {.columns}" /C:"::::" "c:\Users\jfimb\Dropbox\Teaching\LLM\LLMsInFinance\src\day2\lecture\04-tracing-thoughts.qmd" | find /C "::::"

echo.
echo Done. Check results above for each file.
pause
