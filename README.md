# AI Professional Skills Course

This repository contains materials, notebooks, and scripts for a practical course designed to build real-world AI development skills.

## 🚀 Course Objectives

- Set up a full AI-ready dev environment on Windows with WSL2
- Learn to use Git, Python, Jupyter, and popular AI libraries effectively
- Develop, test, and run ML and AI projects locally and in the cloud
- Integrate tools like OpenAI APIs and LangChain into real use cases

## 🗂️ Project Structure

```
ai-professional-skills/
├── notebooks/          # Jupyter notebooks per lesson/module
├── scripts/            # Python utility scripts
├── data/               # Local datasets (not tracked in Git)
├── models/             # Trained models (ignored in Git)
├── .github/workflows/  # GitHub Actions CI
├── .env                # API keys and secrets (ignored)
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md
```

## 🧪 Requirements

- Python 3.10+
- Git + GitHub account
- VS Code (recommended)
- An OpenAI API key (for some modules)

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔐 API Keys

Store API keys in a `.env` file like this:

```env
OPENAI_API_KEY=your-api-key-here
```

> ⚠️ Never commit real keys to GitHub.

## ⚙️ GitHub Actions

This repo includes a GitHub Actions workflow that:
- Installs dependencies
- Converts notebooks to scripts for linting

You can expand it to run tests, deploy models, or more.

## 📚 License

MIT License — use and adapt freely, with attribution.
