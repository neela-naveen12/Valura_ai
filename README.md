# 💰 Valura AI — Intelligent Wealth Co-Investor Microservice

## 📌 Overview

Valura AI is a FastAPI-based microservice designed to act as an **AI co-investor**, helping users **build, monitor, grow, and protect** their investments.

This project implements the **core spine of the system**:

* Safety Guard (rule-based, low latency)
* Intent Classifier (LLM-driven)
* Agent Router
* Portfolio Health Check Agent (fully implemented)
* Streaming responses using Server-Sent Events (SSE)

---

## 🚀 Features

### ✅ Safety Guard

* Blocks harmful financial requests (insider trading, manipulation, etc.)
* Runs locally (no LLM, <10ms latency)
* Returns category-specific responses

### ✅ Intent Classifier

* Single LLM call
* Extracts:

  * intent
  * entities (tickers, amounts)
  * target agent
  * safety verdict
* Handles follow-up queries using session memory

### ✅ Portfolio Health Agent

* Analyzes user portfolio
* Outputs:

  * concentration risk
  * performance metrics
  * benchmark comparison
  * actionable insights
* Handles empty portfolios gracefully (BUILD guidance)

### ✅ Streaming (SSE)

* Real-time response streaming
* Improves perceived latency and UX

### ✅ Frontend (Streamlit)

* Simple UI for testing queries
* Displays streaming responses

---

## 🏗️ Architecture

User Query
→ Safety Guard
→ Intent Classifier (LLM)
→ Router
→ Agent (Portfolio Health / Stub)
→ SSE Streaming Response

---

## 📁 Project Structure

```
src/
  agents/
  core/
  models/
  routes/
tests/
frontend/
README.md
requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Create Virtual Environment

```
python -m venv navin
navin\Scripts\activate
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run Backend

```
python -m uvicorn src.main:app --reload
```

### 4. Run Frontend

```
streamlit run frontend/app.py
```

---

## 🧪 Running Tests

```
pytest tests/ -v
```

---

## 📥 API Usage

### Endpoint:

POST /query

### Sample Request:

```
{
  "query": "How is my portfolio?",
  "session_id": "user1",
  "portfolio": [
    {"ticker": "AAPL", "value": 60000},
    {"ticker": "TSLA", "value": 20000}
  ]
}
```

---

## ⚠️ Safety Design

* Safety Guard is the **only blocking layer**
* Classifier safety verdict is informational only
* Educational queries are allowed

---

## ⚡ Performance Considerations

* Single LLM call per request
* Lightweight rule-based safety
* Streaming reduces perceived latency
* Designed for <2s first-token latency

---

## 🔄 Tradeoffs

* Used in-memory session storage (simpler, faster for demo)
* Stub agents for extensibility
* Basic market data (can be improved with real APIs)

---

## 🚀 Future Improvements

* Add more agents (market research, strategy, risk)
* Improve classifier accuracy with fine-tuning
* Add caching layer
* Better portfolio analytics
* Production-grade persistence (Postgres)

---

## ⚠️ Disclaimer

This system is for educational purposes only.
It does not provide financial advice.

---

## 🎥 Demo Video

(Add your video link here)

---

## 👨‍💻 Author

Neela Naveen
