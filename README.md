# 🧠 Autonomous Goal-Driven Agent

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Powered-000000?style=for-the-badge&logoColor=white)
![LLaMA](https://img.shields.io/badge/LLaMA_3-Meta-0064E0?style=for-the-badge&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)

**A structured, autonomous AI agent that thinks in phases — Plan → Execute → Reflect → Synthesize → Stop**

[Overview](#-overview) · [Architecture](#-architecture) · [Getting Started](#-getting-started) · [Deployment](#-deployment-streamlit-cloud) · [Project Structure](#-project-structure)

</div>

---

## 📌 Overview

This project implements a **single-service autonomous AI agent** with a clean, phase-driven control loop. Unlike naive prompt-chaining or simple chatbot apps, each reasoning phase is handled by a **distinct role**, improving reliability, auditability, and output quality.

The agent accepts a user-defined goal, thinks step-by-step, reflects on its own progress, and halts intelligently — all powered by **Groq's ultra-fast LLM inference** and a **Streamlit** frontend.

### ✨ Key Highlights

- 🎯 Goal-oriented task decomposition via a structured Planner
- 🔁 Iterative execution with per-step reflection
- 🛑 Self-terminating loop with configurable step limits
- 📄 Final synthesis of all execution history into a clean answer
- ⚡ Near-instant inference via Groq API + LLaMA 3

---

## 🏗 Architecture

The agent follows a strict, sequential reasoning pipeline:

```
User Goal
    │
    ▼
┌─────────────┐
│   Planner   │  ← Breaks goal into actionable steps
└──────┬──────┘
       │
       ▼
┌──────────────────────────────────────┐
│            Execution Loop            │
│                                      │
│   ┌──────────┐     ┌─────────────┐   │
│   │ Executor │────▶│  Reflector  │   │
│   └──────────┘     └──────┬──────┘   │
│                           │          │
│              Continue or STOP        │
└───────────────────────────┼──────────┘
                            │
                            ▼
                   ┌─────────────────┐
                   │   Synthesizer   │  ← Consolidates all results
                   └────────┬────────┘
                            │
                            ▼
                      Final Answer
```

### Agent Roles

| Role | Symbol | Responsibility |
|------|--------|----------------|
| **Planner** | 🧭 | Decomposes the user's goal into a structured, ordered list of actionable steps |
| **Executor** | ⚙️ | Carries out one step at a time, producing intermediate results |
| **Reflector** | 🪞 | Evaluates whether sufficient progress has been made; decides to continue or stop |
| **Stop Controller** | 🛑 | Hard safeguard that enforces a maximum step limit to prevent infinite loops |
| **Synthesizer** | 📄 | Aggregates all execution history into a final, coherent answer |

---

## ⚙️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.10+** | Core application language |
| **Streamlit** | Web UI and cloud deployment |
| **Groq API** | High-speed LLM inference backend |
| **LLaMA 3 (via Groq)** | Reasoning, planning, and synthesis |

---

## 📁 Project Structure

```
goal-driven-agent/
│
├── app.py                  # Streamlit UI — entry point
├── agent.py                # Core agent logic (Planner, Executor, Reflector, Synthesizer)
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
└── .streamlit/
    └── secrets.toml        # Local secrets — NOT committed to version control
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- A valid [Groq API key](https://console.groq.com)

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/goal-driven-agent.git
cd goal-driven-agent
```

### 2. Create a Virtual Environment

```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Your API Key

Create the secrets file at `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

> ⚠️ **Never commit this file.** Ensure `.streamlit/secrets.toml` is listed in your `.gitignore`.

### 5. Run the App

```bash
streamlit run app.py
```

The application will open at `http://localhost:8501` in your browser.

---

## 🌍 Deployment (Streamlit Cloud)

1. **Push** your repository to GitHub (ensure `secrets.toml` is in `.gitignore`)
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign in
3. Click **New App** and select your repository
4. Set `app.py` as the entry point
5. Navigate to **Advanced Settings → Secrets** and add:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

6. Click **Deploy** — your app will be live within minutes

---

## 🔐 Environment Variables

| Variable | Description | Required |
|---|---|---|
| `GROQ_API_KEY` | Your Groq API key for LLM inference | ✅ Yes |

---

## 🧩 Agent Design — Deep Dive

### 🧭 Planner
Receives the user's raw goal and produces a structured, ordered execution plan. Ensures that complex goals are broken into discrete, achievable steps before any execution begins.

### ⚙️ Executor
Takes a single step from the plan and executes it, producing an intermediate result. Operates without awareness of other steps to maintain clean separation of concerns.

### 🪞 Reflector
After each execution step, the Reflector evaluates whether the goal has been sufficiently addressed. It can emit a `CONTINUE` or `STOP` signal based on the quality and completeness of the accumulated results.

### 🛑 Stop Controller
An independent safeguard that enforces a configurable maximum number of steps. This prevents the agent from looping indefinitely if the Reflector fails to emit a `STOP` signal.

### 📄 Synthesizer
Once the loop terminates, the Synthesizer receives the full execution history and produces a final, consolidated, human-readable answer — ensuring the output is coherent and not just a raw dump of intermediate results.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Please open an issue first to discuss what you would like to change.

---

<div align="center">

Built with ⚡ [Groq](https://groq.com) · 🖥️ [Streamlit](https://streamlit.io) · 🦙 LLaMA 3

</div>