# Context Guardian — Prevent Miscommunication Agent

## Overview
A lightweight, unique multi-agent system that detects ambiguous/unclear chat messages and rewrites them into clear, actionable text. Built to be fast to implement and easy to demo for the Kaggle Agents Capstone.

## Features
- Interpretation Agent: parses and extracts intents / missing fields
- Risk Detection Agent: finds ambiguity, missing deadlines, missing recipients
- Correction Agent: rewrites message into a clear version (LLM-enabled or heuristic fallback)
- Memory Agent: stores user preferences and common corrections
- Loop Agent: asks for confirmation and refines the message

## Run locally
1. Create a Python environment (recommended: venv)

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

2. Run the demo:

```bash
python src/main.py
```

This will run a quick interactive demo where you type a message and the agent pipeline analyzes and suggests improvements. You can also run with `-e` to enable LLM if you wire up `LLM_API_KEY` in `.env` (see note below).

## Notes about LLM usage
- The repo includes a `utils/llm_wrapper.py` with a stubbed `call_llm(prompt)` function.
- To use a real LLM, replace the stub with an API call to your preferred model and set the API key in `.env` (do NOT commit keys to GitHub).

## Kaggle Submission tips
- Add `README.md` describing architecture, features, and instructions
- Add inline comments in code (already provided)
- Record a short <3 min demo video showing the interactive flow


# Context Guardian — AI Agent for Clear & Unambiguous Communication  
### Kaggle Agents Intensive — Capstone Project (Enterprise Track)

---

## 🌟 Overview  
**Context Guardian** is a multi‑agent system that detects unclear, ambiguous, or incomplete user messages and rewrites them into **clear, actionable, and professional communication**.  
It acts as an AI “clarity layer” for messaging — ensuring recipients always know **who**, **what**, and **when**.

This project is built specifically for the **Kaggle Agents Intensive Capstone**, demonstrating agent orchestration, LLM‑powered rewriting, memory, risk analysis, and refinement loops.

---

## 🚀 Key Features

### 🧠 1. Interpretation Agent  
Extracts:
- verbs  
- recipients  
- time expressions  
- missing structural elements  

This provides a structured semantic representation of the raw message.

---

### ⚠️ 2. Risk Detection Agent  
Analyzes clarity & detects:
- ambiguous references  
- missing deadline  
- missing recipient  
- missing action  
- vague context  
- too‑short messages  

Outputs a severity score (low/medium/high).

---

### ✍️ 3. Correction Agent  
Uses **Gemini 2.0 Flash** (or heuristic fallback) to rewrite the message using:
- selected style: *formal*, *friendly*, *brief*, *neutral*  
- strict JSON output  
- placeholders for missing details  
- reduced hallucinations  
- retries + guardrails  

Only `rewritten_text` is returned for a clean UX.

---

### 🔁 4. Feedback Loop Agent  
Implements an evaluation loop:
- asks user to rate clarity (1–5)  
- supports accept / edit / refine  
- re‑invokes the LLM for improvements  

---

### 🧬 5. Memory Agent  
Stores:
- past corrections  
- tone/style preferences  
- timestamps  
- clarity scores  

Supports personalization and better future rewrites.

---

## 🧩 Architecture Diagram (Text Version)

```
User Message
      │
      ▼
Intake → Interpretation Agent → Risk Agent
      │            │
      ▼            ▼
  Loop Agent ← Correction Agent (LLM or fallback)
      │
      ▼
   Memory Agent (history + preferences)
      │
      ▼
 Final Rewritten Message
```

---

## 🛠️ Technology Used  
- **Python**  
- **Gemini 2.0 Flash API**  
- **Multi‑Agent Pipeline (custom)**  
- **JSON‑structured LLM outputs**  
- **Retry logic, guardrails, memory persistence**  
- **CLI interactive demo**

This satisfies >3 required features from the Kaggle rubric:
- Multi‑agent system  
- Tools (LLM wrapper, memory, risk engine)  
- Observability (debug mode, JSON output mode)  
- Sessions & state (memory)  

---

## ▶️ Running the Project Locally

### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. (Optional) Enable LLM Mode  
Create `.env`:
```
LLM_PROVIDER=gemini
LLM_API_KEY=YOUR_API_KEY
```

### 4. Run the interactive demo
```bash
python src/main.py
```

Flags:
```
-d  --debug      # detailed logs
-j  --json       # structured JSON output
-e  --enable-llm # use Gemini instead of heuristic mode
```

---

## 📁 Repository Structure  
```
context_guardian_full/
│
├── src/
│   ├── agents/
│   │   ├── intake_agent.py
│   │   ├── interpretation_agent.py
│   │   ├── risk_agent.py
│   │   ├── correction_agent.py
│   │   ├── loop_agent.py
│   │   └── memory_agent.py
│   ├── utils/
│   │   └── llm_wrapper.py
│   └── main.py
│
├── memory_bank.json        # auto‑generated
├── requirements.txt
├── architecture.txt
├── video_script.md
└── README.md
```

---

## 🎯 Why This Project Fits the Enterprise Track  
Modern teams suffer from miscommunication — unclear messages lead to delays, mistakes, and frustration.

Context Guardian solves this with:
- automatic message clarification  
- tone control  
- ambiguity detection  
- professional rewriting  
- memory‑based personalization  

Ideal for:
- teams  
- Slack/Teams integrations  
- support desks  
- workflow automation  

---

## 🏁 Bonus Points (Recommended Enhancements)
- ✔ LLM (Gemini) integration  
- ✔ Documentation (this README)  
- ✔ Architecture explanation  
- ✔ Short demo video script included in `video_script.md`  

You can record a <3 min video showing:
- Problem  
- Why agents  
- Architecture  
- Pipeline demo  
- Value  

---

## 📢 Final Notes  
This project demonstrates a full, production‑style multi‑agent system built specifically for the Kaggle Agents Capstone.  
It is simple to run, easy to evaluate, and clearly showcases multi‑agent coordination + memory + LLM rewriting.

Happy hacking! 🚀