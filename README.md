# SUPROC AI AGENT

An AI-powered procurement assistant that understands natural language requirements, searches supplier data, ranks the best suppliers, explains every recommendation, and generates outreach drafts with a human approval workflow.

---

# Features

- Natural language procurement queries
- Ollama (Qwen3:4b) powered requirement parsing
- AI planning before execution
- SQLAlchemy + SQLite supplier database
- Exact supplier search
- Closest-match fallback search
- Rule-based supplier validation
- Intelligent supplier ranking
- Explainable AI recommendations
- Automated outreach draft generation
- Human approval workflow

---

# Tech Stack

- Python 3.11+
- Ollama
- Qwen3:4b
- SQLAlchemy
- SQLite
- Pydantic

---

# Project Architecture

```
User
   │
   ▼
Natural Language Requirement
   │
   ▼
Hybrid Parser
(Ollama + Rule Parser)
   │
   ▼
Planning Module
   │
   ▼
Supplier Search
   │
   ├── Exact Search
   │
   └── Closest Match Search
   │
   ▼
Validation
   │
   ▼
AI Ranking Engine
   │
   ▼
Explainability Layer
   │
   ▼
Outreach Generator
   │
   ▼
Human Approval
```

---

# Project Structure

```
suproc-agent/

├── data/
│   └── suproc.db
│
├── src/
│   ├── agent/
│   ├── database/
│   ├── llm/
│   ├── models/
│   ├── tools/
│   └── utils/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

### Clone Repository

```bash
git clone <repository-url>
cd suproc-agent
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment (Windows)

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

https://ollama.com/

### Download Model

```bash
ollama pull qwen3:4b
```

### Start Ollama

```bash
ollama serve
```

---

# Run Project

```bash
python main.py
```

---

# Example Queries

```
Need food grade packaging supplier in Tamil Nadu with capacity 10000 delivery in 30 days

Need biodegradable raw material supplier in Kerala

Need logistics company in Telangana

Need packaging supplier in Karnataka
```

---

# AI Workflow

1. Parse the user's natural language request.
2. Generate an execution plan.
3. Search for exact supplier matches.
4. If no exact match exists, search for closest suppliers.
5. Validate supplier records.
6. Calculate AI-based supplier scores.
7. Explain every recommendation.
8. Generate outreach messages.
9. Wait for human approval.

---

# Supplier Ranking Factors

The AI ranking engine evaluates suppliers using:

- Category Match
- Location Match
- Certification Match
- Capacity
- Delivery Time
- Supplier Rating
- Sustainability Score
- Availability

---

# Explainable AI

Every recommendation includes:

- Matched requirements
- Unmatched requirements
- Evidence used for scoring
- Final AI score

---

# Sample Output

```
Rank #1

Supplier : Mallick-Bains

Score : 88.70

Match Type : Closest Match

Matched:
✔ Category
✔ Certification
✔ Capacity
✔ Delivery

Not Matched:
✘ Location
```

---

# Human Approval

The AI never contacts suppliers automatically.

Instead, it generates an outreach draft and waits for manual approval before any communication.

---

# Known Limitations

• Synthetic dataset
• No live supplier APIs
• CLI interface
• No email integration

---

# Future Improvements

- Live supplier APIs
- Email integration
- Multi-agent workflow
- RAG-based supplier search
- Vector database support
- Web dashboard
- PDF proposal generation
- Supplier risk analysis

---

# Author

Developed as an AI Procurement Agent using Python, SQLAlchemy, SQLite, and Ollama (Qwen3:4b).
