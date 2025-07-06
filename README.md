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

The course is organized into 5 days, with currently available materials for Day 0 and Day 1:

### 📌 Day 0: Course Introduction
- **Lecture**: Instructor introduction, course overview, learning outcomes

### 📌 Day 1: Introduction to Large Language Models
- **Lecture**: Introduction to LLMs, architectures, capabilities, and limitations
- **Practical**: 
  - Environment setup and package installation
  - Git and version control
  - HuggingFace setup
  - LLM APIs

#### Day 1 Practical Notebooks

1. **Environment Setup**
   - Python environment setup
   - Installing required packages
   - Testing the environment

2. **Git and Version Control**
   - Git repository setup
   - Best practices for version control
   - API key security with `.gitignore`

3. **HuggingFace Setup**
   - Local model usage with HuggingFace
   - Model loading and optimization
   - Financial sentiment analysis example

4. **LLM APIs**
   - OpenAI API integration
   - Other API integrations
   - Environment variable management
   - Financial news sentiment analyzer project

#### Automated Setup Options

For Day 1 practical session, you can use:
- Windows: Run `setup.bat` in the day1/practical-session directory
- macOS/Linux: Run `bash setup.sh` in the day1/practical-session directory

## 🛠️ Technical Requirements

### Prerequisites
- Python 3.10+
- Git
- Jupyter notebook environment
- API keys for LLM services (OpenAI/etc.)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/jfimbett/LLMsInFinance.git
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
     HUGGINGFACE_API_KEY=your_huggingface_key_here
     ```

   > **Note on API Usage**: Some notebooks use the OpenAI API and other commercial services. Please be aware of potential usage costs when running certain cells. Free tier limits may be sufficient for educational purposes, but monitor your usage.

5. Launch Jupyter for the practical sessions:
   ```bash
   jupyter notebook
   ```

## 📂 Repository Structure

```
LLMsInFinance/
├── LICENSE
├── README.md
├── requirements.txt
├── src/
│   ├── day0/           # Course introduction
│   ├── day1/           # Introduction to Large Language Models
│   ├── images/         # Shared images for lectures and notebooks
```

Each day folder contains:
- `lecture/`: Presentation materials in HTML format
- `practical-session/` (where applicable): Jupyter notebooks with hands-on exercises

## 🤝 Contributing

Contributions to improve the course materials are welcome. Please feel free to submit a pull request or open an issue.

## ❓ Troubleshooting

If you encounter issues while setting up or running the course materials:

- **Environment Setup**:
  - Ensure you have the correct Python version (3.10+)
  - Try creating a fresh virtual environment
  - Check that all dependencies are installed correctly

- **API Connectivity**:
  - Verify your API keys are correctly set in the `.env` file
  - Check your internet connection
  - Ensure you have sufficient quota/credits for the API services

- **Jupyter Notebooks**:
  - If cells are slow to execute, consider reducing model sizes or batch sizes
  - For memory errors, restart the kernel and run only essential cells
  - Use `%debug` magic command to troubleshoot errors in code cells

For additional help, please open an issue on the GitHub repository.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

Juan F. Imbet - Course Instructor
   - Create caching mechanisms for efficient LLM usage
   - Develop automatic function calling for financial applications
   - Build a financial assistant with memory and tool use capabilities

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

#### Day 4 Practical Notebooks

1. **Fine-tuning for Default Probability**
   - Learn how to fine-tune a BERT model for predicting loan default probabilities
   - Data preparation, training, evaluation, and calibration of output probabilities
   - Create specialized financial risk models

2. **Simulating Household Decisions**
   - Use LLMs to simulate complex household financial decision-making processes
   - Analyze how different types of households respond to changing economic conditions
   - Model diverse financial behaviors with agent-based approaches

3. **Building a Mortgage Rate Estimator**
   - Develop a practical web application using Flask
   - Leverage both traditional machine learning and LLMs
   - Estimate personalized mortgage rates based on client profiles
   - Create interactive financial tools

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
     HUGGINGFACE_API_KEY=your_huggingface_key_here
     ```

   > **Note on API Usage**: Some notebooks use the OpenAI API and other commercial services. Please be aware of potential usage costs when running certain cells. Free tier limits may be sufficient for educational purposes, but monitor your usage.

5. Launch Jupyter for the practical sessions:
   ```bash
   jupyter notebook
   ```

6. Each day's practical session has its own additional setup requirements. See the respective Jupyter notebooks for details.

## 📘 Preliminaries

If you're new to Python or need a refresher on the fundamentals, check out the Preliminaries section in `src/preliminaries/`, which includes:

- A comprehensive [Python Crash Course](src/preliminaries/01-python-crash-course.ipynb) with NumPy and PyTorch
- Introduction to vectors and tensors for neural networks
- Basic neural network concepts for understanding LLMs

### Preliminaries Learning Objectives

After going through the Python crash course, you should be able to:

1. Understand basic Python syntax and data structures
2. Use NumPy for numerical computing with arrays
3. Create and manipulate tensors with PyTorch
4. Understand the tensor operations used in neural networks
5. Build simple neural network models with PyTorch

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

## ❓ Troubleshooting

If you encounter issues while setting up or running the course materials:

- **Environment Setup**:
  - Ensure you have the correct Python version (3.10+)
  - Try creating a fresh virtual environment
  - Check that all dependencies are installed correctly

- **API Connectivity**:
  - Verify your API keys are correctly set in the `.env` file
  - Check your internet connection
  - Ensure you have sufficient quota/credits for the API services

- **GPU Acceleration**:
  - Verify your CUDA installation if using GPU acceleration
  - Check PyTorch/TensorFlow is installed with GPU support
  - Run the test scripts in the root directory to verify

- **Jupyter Notebooks**:
  - If cells are slow to execute, consider reducing model sizes or batch sizes
  - For memory errors, restart the kernel and run only essential cells
  - Use `%debug` magic command to troubleshoot errors in code cells

For additional help, please open an issue on the GitHub repository.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
