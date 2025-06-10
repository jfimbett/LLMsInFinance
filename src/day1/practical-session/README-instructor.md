# Instructor Notes: Day 1 Practical Session

This document provides additional context and guidance for instructors leading the Day 1 practical session.

## Session Overview

The Day 1 practical session covers the foundational skills needed for working with LLMs:
1. Environment setup
2. Version control
3. HuggingFace model usage
4. API integration (OpenAI and DeepSeek)

## Key Learning Outcomes

By the end of this practical session, students should be able to:
- Create and manage Python environments for LLM projects
- Understand and implement best practices for version control (especially for sensitive data)
- Load and use HuggingFace models locally
- Access LLMs through APIs securely
- Apply these skills to simple financial analysis tasks

## Preparation Before Class

1. **API Keys**: Ensure students know they need to obtain their own API keys:
   - OpenAI: https://platform.openai.com/api-keys
   - DeepSeek: https://platform.deepseek.com/

2. **Environment**: Verify the lab computers have:
   - Python 3.10+ installed
   - Git installed
   - Jupyter environment available
   - Sufficient RAM for smaller models (min 8GB)

3. **Notebook Testing**: Run through all notebooks before class to ensure:
   - All required packages can be installed
   - Models load properly
   - API connections work

## Teaching Notes

### Common Issues

1. **API Key Management**:
   - Students often struggle with .env files and .gitignore
   - Emphasize security best practices multiple times

2. **Environment Setup**:
   - venv vs. conda confusion
   - Package installation errors
   - GPU vs. CPU considerations

3. **Model Loading**:
   - Memory issues with larger models
   - First-time downloads can be slow
   - HuggingFace token requirements

4. **Version Control**:
   - Accidentally committing API keys
   - Merge conflicts in shared repositories

### Content from Original QMD Files

Note: The Jupyter notebooks have been created to replace the original .qmd files, but some valuable content from the QMD files has been preserved in the notebooks:

1. From `01-python-environment.qmd`:
   - Virtual environment explanation
   - Conda setup instructions
   - Requirements.txt examples

2. From `02-version-control.qmd`:
   - Git basics
   - .gitignore configuration
   - API key security

3. From `03-huggingface-intro.qmd`:
   - HuggingFace ecosystem overview
   - Model size considerations
   - Financial model examples

4. From `04-llm-apis.qmd`:
   - API key management
   - Provider comparisons
   - Security best practices

## Time Management

Suggested time allocation for a 3-hour session:
- 30 min: Introduction and environment setup
- 30 min: Version control setup
- 45 min: HuggingFace models
- 45 min: API integration
- 30 min: Final project and questions

## Action Needed: QMD Files

**Decision Required**: The original QMD files (`01-python-environment.qmd`, `02-version-control.qmd`, etc.) have been replaced with more comprehensive Jupyter notebooks. You need to decide whether to:

1. Remove the original QMD files as they're now redundant
2. Keep them for reference but mark them as deprecated
3. Update them to redirect users to the new notebooks

Recommendation: Either remove them completely or add a notice at the top of each QMD file redirecting users to the corresponding notebook.

## Additional Resources

- Course GitHub Repository: [LLMsInFinance](https://github.com/yourusername/LLMsInFinance)
- Alternative to HuggingFace (if issues): [Ollama](https://ollama.ai/) for local models
- Budget-friendly API alternative: [Claude API](https://www.anthropic.com/claude) or [Cohere](https://cohere.com/)
