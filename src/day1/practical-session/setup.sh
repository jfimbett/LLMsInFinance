#!/bin/bash
# Setup script for Day 1 LLMs in Finance practical session

echo "Setting up environment for LLMs in Finance practical session..."

# Create virtual environment
echo "Creating Python virtual environment..."
python -m venv venv
source venv/bin/activate

# Install requirements
echo "Installing required packages..."
pip install -r requirements.txt

# Create .env file from example if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "Please edit the .env file to add your API keys."
else
    echo ".env file already exists."
fi

echo "Setup complete!"
echo
echo "Next steps:"
echo "1. Edit .env to add your API keys"
echo "2. Run 'jupyter notebook' to start Jupyter"
echo "3. Open the 01-environment-setup.ipynb notebook"

read -p "Press Enter to continue..."
