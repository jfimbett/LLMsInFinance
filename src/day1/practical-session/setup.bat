@echo off
REM Setup script for Day 1 LLMs in Finance practical session

echo Setting up environment for LLMs in Finance practical session...

REM Create virtual environment
echo Creating Python virtual environment...
python -m venv venv
call venv\Scripts\activate

REM Install requirements
echo Installing required packages...
pip install -r requirements.txt

REM Create .env file from example if it doesn't exist
if not exist .env (
    echo Creating .env file from template...
    copy .env.example .env
    echo Please edit the .env file to add your API keys.
) else (
    echo .env file already exists.
)

echo Setup complete! 
echo.
echo Next steps:
echo 1. Edit .env to add your API keys
echo 2. Run 'jupyter notebook' to start Jupyter
echo 3. Open the 01-environment-setup.ipynb notebook

pause
