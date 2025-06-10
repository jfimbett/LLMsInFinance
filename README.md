# LLMs in Finance

Repository for the course "Large Language Models in Finance" - Barcelona School of Economics (BSE) Summer School 2025. This repository contains all the materials for both the lectures and practical sessions.

## 📚 Course Overview

This 5-day intensive course explores the application of Large Language Models (LLMs) in financial contexts. From foundational concepts to advanced applications, the course provides both theoretical knowledge and hands-on experience with state-of-the-art language models for financial analysis, sentiment prediction, risk assessment, and more.

### Learning Objectives

By the end of this course, you will be able to:

- Understand the architecture and capabilities of modern LLMs
- Apply LLMs to various financial use cases using appropriate prompt engineering techniques
- Evaluate and mitigate limitations and biases in LLM applications for finance
- Implement advanced techniques including fine-tuning and structured generation
- Design and develop practical LLM-powered applications for financial analysis

## 🗓️ Course Structure

The course is organized into 5 days, each with lecture materials and hands-on practical sessions:

### 📌 Day 0: Course Introduction
- **Lecture**: Instructor introduction, course overview, learning outcomes
- **Practical**: Environment setup, course materials access, first LLM interaction

### 📌 Day 1: Getting Started with LLMs
- **Lecture**: Introduction to LLMs, architectures, capabilities, and limitations
- **Practical**: 
  - Environment setup and package installation
  - Git and version control
  - HuggingFace model usage
  - OpenAI and DeepSeek API integration

### 📌 Day 2: LLMs for Financial Analysis
- **Lecture**: LLMs for financial texts, sentiment analysis, information extraction
- **Practical**: 
  - Financial sentiment analysis
  - Named entity recognition in financial documents
  - Report summarization and information extraction

### 📌 Day 3: Prompt Engineering for Finance
- **Lecture**: Prompt engineering principles, techniques, and best practices
- **Practical**: 
  - Basic and advanced prompting techniques
  - Few-shot learning and chain-of-thought prompting
  - Custom financial prompt templates
  - Prompt optimization strategies

### 📌 Day 4: Fine-tuning and Specialized Models
- **Lecture**: Understanding credit risk, model fine-tuning, domain adaptation
- **Practical**: 
  - Model fine-tuning techniques
  - Domain-specific adaptations
  - Financial data preprocessing
  - Evaluation metrics and validation approaches

### 📌 Day 5: Advanced Applications and Future Directions
- **Lecture**: Forecasting returns with LLMs, AI in asset management, reinforcement learning
- **Practical**: 
  - Current state of AI: capabilities and limitations
  - Structured generation for information retrieval
  - Beyond text: architecture of text-to-image models

## 🛠️ Technical Requirements

### Prerequisites
- Python 3.10+
- Git
- Jupyter notebook environment
- API keys for LLM services (OpenAI/DeepSeek)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/username/LLMsInFinance.git
   cd LLMsInFinance
   ```

2. Create and activate a virtual environment:
   ```bash
   # For Windows
   python -m venv venv
   venv\Scripts\activate

   # For macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your API keys:
   - Create a `.env` file in the root directory
   - Add your API keys (do not commit this file to version control):
     ```
     OPENAI_API_KEY=your_openai_key_here
     DEEPSEEK_API_KEY=your_deepseek_key_here
     ```

## 📘 Preliminaries

If you're new to Python or need a refresher on the fundamentals, check out the [Preliminaries](src/preliminaries/README.md) section, which includes:

- A comprehensive [Python Crash Course](src/preliminaries/01-python-crash-course.ipynb) with NumPy and PyTorch
- Introduction to vectors and tensors for neural networks
- Basic neural network concepts for understanding LLMs

This material will help you get up to speed before diving into the main course content.

## 📂 Repository Structure

```
LLMsInFinance/
├── LICENSE
├── README.md
├── requirements.txt
├── src/
│   ├── day0/           # Course introduction
│   ├── day1/           # Getting Started with LLMs
│   ├── day2/           # LLMs for Financial Analysis
│   ├── day3/           # Prompt Engineering for Finance
│   ├── day4/           # Fine-tuning and Specialized Models
│   ├── day5/           # Advanced Applications and Future Directions
│   ├── images/         # Shared images for lectures and notebooks
│   └── preliminaries/  # Preparatory materials
```

Each day folder contains:
- `lecture/`: Presentation materials in Quarto format
- `practical-session/`: Jupyter notebooks with hands-on exercises

## 🤝 Contributing

Contributions to improve the course materials are welcome. Please feel free to submit a pull request or open an issue.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Repository for the course "Large Language Models in Finance" - Barcelona School of Economics (BSE) Summer School 2025. This repository contains all the materials for both the lectures and practical sessions.

## Course Structure

This course is organized by days, with each day consisting of:
- Lecture materials
- Practical sessions

### Days Overview

- **Day 0**: Course Introduction
- **Day 1**: Getting Started with LLMs
  - Environment setup
  - Version control
  - HuggingFace
  - LLM APIs (OpenAI and DeepSeek)
- **Day 2**: LLMs for Financial Analysis
- **Day 3**: Prompt Engineering for Finance
- **Day 4**: Fine-tuning and Specialized Models
- **Day 5**: Advanced Applications and Future Directions

## Getting Started

For the practical sessions, you'll need:
1. Python 3.10+
2. Git
3. A Jupyter notebook environment
4. API keys for LLM services (OpenAI/DeepSeek)

See each practical session's README for specific setup instructions.

## Preliminaries

If you're new to Python or need a refresher on the fundamentals needed for this course, check out the [Preliminaries](src/preliminaries/README.md) section, which includes:

- A comprehensive [Python Crash Course](src/preliminaries/01-python-crash-course.ipynb) with NumPy and PyTorch
- Introduction to vectors and tensors for neural networks
- Basic neural network concepts for understanding LLMs

This material will help you get up to speed before diving into the main course content.

## Day 1 Practical Session

The Day 1 practical session now includes comprehensive Jupyter notebooks covering:
- Python environment setup
- Git and version control
- Local model usage with HuggingFace
- API integration with OpenAI and DeepSeek

See the [Day 1 Practical Session](src/day1/practical-session/README.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
