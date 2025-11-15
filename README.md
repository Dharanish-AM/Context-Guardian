# Context Guardian — AI Agent for Clear & Actionable Communication  
A lightweight, multi‑agent system that transforms unclear or ambiguous chat messages into clear, structured, and actionable communication.  
Built for the **Kaggle Agents Intensive — Capstone Project (Enterprise Track)** and refined for real‑world team communication workflows.

---

## 📌 Overview
Modern teams lose time and productivity because of vague messages like:

- “Send that file soon”
- “Fix this ASAP”
- “Check this”

These messages lack **context**, **recipients**, **deadlines**, and **specific actions**.

**Context Guardian** solves this by using a multi‑agent architecture that analyzes message clarity, detects missing information, rewrites the message professionally, and personalizes tone using memory.

It serves as an AI-powered *communication clarity layer* for daily messaging.

---

## 🚀 Key Features  
### 🧠 Interpretation Agent  
Extracts:
- verbs  
- actions  
- recipients  
- time expressions  
- missing structural components  

### ⚠️ Risk Detection Agent  
Identifies:
- ambiguity  
- missing deadlines  
- missing recipients  
- vague references  
- unclear intent  
- too-short messages  
- overall clarity score  

### ✍️ Correction Agent  
Rewrites messages using:
- **Gemini 2.0 Flash** (or heuristic fallback)  
- selected tone: *formal*, *friendly*, *brief*, *neutral*  
- strict JSON output cleaning  
- retry logic + hallucination reduction  
- placeholders for missing details  

### 🔁 Loop Agent  
Interactive refinement loop:
- shows a rewritten suggestion  
- user rates clarity (1–5)  
- accepts or requests refinement  

### 🧬 Memory Agent  
Stores:
- past corrections  
- tone preferences  
- clarity history  
- timestamps  

Personalizes future rewriting automatically.

---

## 🧩 Architecture (Text Diagram)

```
User Message
      │
      ▼
Intake Agent
      │
      ▼
Interpretation Agent → Risk Agent
      │                │
      ▼                ▼
     Loop Agent ← Correction Agent
      │
      ▼
  Memory Agent
      │
      ▼
Final Rewritten Message
```

---

## 🛠️ Tech Stack  
- **Python**  
- **Gemini 2.0 Flash API** (optional)  
- Multi‑Agent pipeline  
- JSON‑structured outputs  
- Retry logic + guardrails  
- Memory persistence (JSON file)  
- CLI interactive demo  

---

## ▶️ Run Locally  
### 1. Create a virtual environment  
```bash
python -m venv venv
source venv/bin/activate    # macOS / Linux
venv\Scripts\activate       # Windows
```

### 2. Install dependencies  
```bash
pip install -r requirements.txt
```

### 3. (Optional) Enable LLM Mode  
Create a `.env` file:
```
LLM_PROVIDER=gemini
LLM_API_KEY=YOUR_API_KEY
```

### 4. Run the demo  
```bash
python src/main.py
```

Flags:
```
-e   --enable-llm   Use Gemini instead of heuristic rewrite
-d   --debug        Show pipeline debug logs
-j   --json         Print structured output
```

---

## 📁 Repository Structure  

```
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
├── memory_bank.json
├── requirements.txt
├── architecture.txt
└── README.md
```

---

## 🎯 Why It Fits the Enterprise Track
Enterprises struggle with unclear communication.  
Context Guardian solves this by providing:

- automatic message clarity  
- structured rewriting  
- customizable tone  
- ambiguity detection  
- memory‑based personalization  
- multi‑agent coordination  

Ideal for:
- Slack / Teams integrations  
- internal tools  
- support teams  
- workflow automation  

---

## 🏁 Bonus Project Assets  
- Architecture diagram  
- Memory system  
- LLM-ready wrapper  
- Full multi-agent breakdown  

---

## 📢 Final Notes  
Context Guardian is a production‑style multi‑agent system that demonstrates:

- agent orchestration  
- LLM tool usage  
- memory  
- observability  
- practical enterprise value  

Simple to run, fun to test, and perfectly aligned with the Kaggle Agents Capstone.

🚀 **Happy building!**