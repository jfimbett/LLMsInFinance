# Practical Session: Day 3 - LLMs in Finance

Welcome to the practical session for Day 3 of the "LLMs in Finance" course. This session focuses on applying Large Language Models (LLMs) to various financial analysis tasks, including document analysis, forecasting, and valuation.

## Notebooks Overview

### 1. [Reading Large Financial Documents](01-reading-large-financial-documents.ipynb)
- **Objective**: Learn how to process and analyze large financial documents using LLMs.
- **Key Topics**:
  - Chunking strategies for large documents.
  - Retrieval-Augmented Generation (RAG) for targeted analysis.
  - Extracting structured information, financial metrics, and forward-looking statements.
  - Summarization techniques and best practices.

### 2. [Forecasting Cashflows](02-forecasting-cashflows.ipynb)
- **Objective**: Generate and evaluate cashflow forecasts using LLMs.
- **Key Topics**:
  - Loading and preprocessing historical financial data.
  - Generating cashflow forecasts.
  - Evaluating forecast accuracy.

### 3. [Selecting Comparables](03-selecting-comparables.ipynb)
- **Objective**: Identify and analyze comparable companies for valuation purposes.
- **Key Topics**:
  - Using LLMs to identify comparable companies based on textual descriptions and financial metrics.
  - Analyzing financial metrics of selected comparables.
  - Deriving valuation insights.

### 4. [Tesla Valuation Case Study](04-tesla-valuation-case-study.ipynb)
- **Objective**: Perform a valuation of Tesla using DCF and multiples-based methods.
- **Key Topics**:
  - Forecasting cashflows for Tesla.
  - Performing DCF valuation.
  - Using comparable company multiples for cross-checking.
  - Conducting scenario analysis with LLMs.

### 5. [Financial Filing Agents](05-financial-filing-agents.ipynb)
- **Objective**: Build a system of specialized agents for analyzing corporate filings.
- **Key Topics**:
  - Creating specialized agents for different financial analysis tasks.
  - Implementing a CrewAI-based workflow for document processing.
  - Extracting insights from 10-Ks and other financial filings.
  - Performing comparative analysis across multiple companies.

## How to Use
1. Open each notebook in sequence to follow the practical session.
2. Ensure you have the required datasets (e.g., `financial_data.csv`, `tesla_financials.csv`) in the same directory.
3. For the financial filing agents notebook, you'll need to provide your own corporate filings.
4. Run the cells step-by-step and explore the outputs.

## Prerequisites
- Python 3.x
- Required libraries: `pandas`, `numpy`, `transformers`, `scipy`, `crewai`, `langchain`
- Install missing libraries using `pip install <library_name>`.

## Notes
- The notebooks are designed to be self-contained and include detailed explanations.
- Feel free to modify the code and experiment with different parameters.
- For the agent-based analysis, you'll need to set up an OpenAI API key.

Happy learning!
