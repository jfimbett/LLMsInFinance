# Day 1 Practical Session: Getting Started with LLMs

This directory contains the practical exercises for Day 1 of the LLMs in Finance course. The practical session focuses on setting up the environment, version control, and connecting to LLM APIs.

## Jupyter Notebooks

The exercises are provided as Jupyter notebooks:

1. **[Environment Setup](01-environment-setup.ipynb)**
   - Python environment setup
   - Installing required packages
   - Testing the environment

2. **[Git and Version Control](02-git-version-control.ipynb)**
   - Git repository setup
   - Best practices for version control
   - API key security with `.gitignore`

3. **[HuggingFace Setup](03-huggingface-setup.ipynb)**
   - Local model usage with HuggingFace
   - Model loading and optimization
   - Financial sentiment analysis example

4. **[LLM APIs](04-llm-apis.ipynb)**
   - OpenAI API integration
   - DeepSeek API integration
   - Environment variable management
   - Financial news sentiment analyzer project

## Setup Instructions

### Prerequisites
- Python 3.10+ installed
- Jupyter notebook environment
- Git installed
- API keys for OpenAI and/or DeepSeek (optional)

### Getting Started

#### Option 1: Automated Setup
1. For Windows: Run `setup.bat`
2. For macOS/Linux: Run `bash setup.sh`
3. Follow the prompts to complete setup

#### Option 2: Manual Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up API keys:
   - Create a `.env` file from the `.env.example` template
   - Add your API keys to the `.env` file
   - Make sure `.env` is in your `.gitignore`

4. Launch Jupyter:
   ```bash
   jupyter notebook
   ```

5. Open the notebooks in order (start with `01-environment-setup.ipynb`)

## Important Notes

- **API Keys Security**: Never commit your API keys to version control. Always use environment variables (.env files) and ensure .env is in your .gitignore.
- **Cost Management**: Be mindful of API usage costs. Set up usage limits in your API provider dashboards.
- **Local vs. API Models**: Start with local models for experimentation, then use API models for more sophisticated tasks.

## Additional Resources

- [HuggingFace Documentation](https://huggingface.co/docs)
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)
- [DeepSeek API Documentation](https://platform.deepseek.com/)
- [Python Environment Management Best Practices](https://realpython.com/python-virtual-environments-a-primer/)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
