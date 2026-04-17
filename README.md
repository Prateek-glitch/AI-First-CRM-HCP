<!-- Minimal animated header -->
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Inter&weight=600&size=24&duration=2800&pause=900&color=0A66C2&center=true&vCenter=true&width=900&lines=AI-First+CRM+HCP+Assistant;FastAPI+%7C+React+%7C+Redux+%7C+LangGraph+%7C+Groq;Log+Interactions%2C+AI+Summaries%2C+Next+Best+Actions" alt="Typing SVG" />
</p>

<h1 align="center">AI-First CRM HCP Assistant</h1>

<p align="center">
AI-powered CRM assistant for managing <b>HCP (Healthcare Professional)</b> interactions, generating AI summaries, and recommending next actions.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Working-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Frontend-React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/State-Redux-764ABC?style=for-the-badge&logo=redux&logoColor=white" />
  <img src="https://img.shields.io/badge/Agent-LangGraph-1F2937?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-Groq-F55036?style=for-the-badge" />
</p>

---

## 📌 Overview

This project helps field reps log doctor interactions quickly using:
- **Structured Form Input**
- **Conversational Agent Intent API**

It combines a standard CRM flow with an AI layer for:
- interaction summarization
- next-step guidance
- follow-up management

---

## 🚀 Core Capabilities

- Log HCP interactions
- Generate AI summaries from notes (Groq LLM)
- Edit interaction records
- Fetch HCP profile details
- Suggest next best actions
- Schedule follow-up tasks

---

## 🧰 Tech Stack

### Backend
<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=flat-square"/>
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white&style=flat-square"/>
  <img alt="SQLAlchemy" src="https://img.shields.io/badge/SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=white&style=flat-square"/>
  <img alt="LangChain" src="https://img.shields.io/badge/LangChain-121D33?style=flat-square"/>
  <img alt="LangGraph" src="https://img.shields.io/badge/LangGraph-111827?style=flat-square"/>
  <img alt="Groq" src="https://img.shields.io/badge/Groq-F55036?style=flat-square"/>
</p>

### Frontend
<p>
  <img alt="React" src="https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB&style=flat-square"/>
  <img alt="Redux" src="https://img.shields.io/badge/Redux-764ABC?logo=redux&logoColor=white&style=flat-square"/>
  <img alt="Vite" src="https://img.shields.io/badge/Vite-646CFF?logo=vite&logoColor=white&style=flat-square"/>
  <img alt="Axios" src="https://img.shields.io/badge/Axios-5A29E4?style=flat-square"/>
</p>

### Database
<p>
  <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white&style=flat-square"/>
  <img alt="SQLite" src="https://img.shields.io/badge/SQLite-07405E?logo=sqlite&logoColor=white&style=flat-square"/>
</p>

> **LLM model used:** `gemma2-9b-it` (Groq)

---

## 🏗️ Architecture

### High-Level Flow
```mermaid
flowchart LR
    A[React + Redux UI] -->|POST /api/agent/chat| B[FastAPI]
    B --> C[LangGraph Intent Router]
    C --> D1[Tool: log_interaction]
    C --> D2[Tool: edit_interaction]
    C --> D3[Tool: fetch_hcp_profile]
    C --> D4[Tool: suggest_next_best_action]
    C --> D5[Tool: schedule_followup]
    D1 --> E[(PostgreSQL/SQLite)]
    D2 --> E
    D3 --> E
    D5 --> E
    D1 --> F[Groq LLM - gemma2-9b-it]
    D4 --> F
    F --> B
    E --> B
    B --> A
```

### Intent Execution Flow
```mermaid
sequenceDiagram
    participant UI as React UI
    participant API as FastAPI /api/agent/chat
    participant LG as LangGraph route_intent
    participant TOOL as Tool Function
    participant DB as Database
    participant LLM as Groq LLM

    UI->>API: { intent, payload }
    API->>LG: invoke(state)
    LG->>TOOL: select tool by intent
    TOOL->>DB: read/write records
    TOOL->>LLM: summary/recommendation (if needed)
    TOOL-->>LG: tool result
    LG-->>API: final state.result
    API-->>UI: JSON response
```

---

## 📁 Repository Structure

```text
backend/
  app/
    api/
      agent.py
      interactions.py
    db/
      session.py
    models/
      hcp.py
      interaction.py
      audit.py
      followup.py
    services/
      llm.py
    tools/
      log_interaction.py
      edit_interaction.py
      fetch_hcp.py
      suggest_nba.py
      schedule_followup.py
    main.py

frontend/
  src/
    api/client.js
    features/
      interaction/InteractionForm.jsx
      chat/AgentChat.jsx
    App.jsx
```

---

## 🛠️ Implemented LangGraph Tools (5)

1. **log_interaction**  
   Creates interaction and generates AI summary.

2. **edit_interaction**  
   Updates selected interaction fields.

3. **fetch_hcp_profile**  
   Returns doctor details from HCP table.

4. **suggest_next_best_action**  
   Provides action suggestions from context/sentiment.

5. **schedule_followup**  
   Creates follow-up task linked to interaction.

---

## ✅ Prerequisites

- Python 3.10+
- Node.js 18+
- npm
- Valid Groq API key

---

## ⚙️ Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create `backend/.env`:

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=gemma2-9b-it
```

Run backend:

```bash
uvicorn app.main:app --reload --port 8000
```

Backend URLs:
- API: `http://127.0.0.1:8000`
- Swagger: `http://127.0.0.1:8000/docs`

---

## 💻 Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend URL:
- `http://localhost:5173`

---

## 🔌 API Contract

### Endpoint
`POST /api/agent/chat`

### Request Body
```json
{
  "intent": "log_interaction",
  "payload": {
    "hcp_id": 1,
    "interaction_type": "Meeting",
    "interaction_date": "2026-04-17",
    "topics_discussed": "Discussed Product X efficacy and phase-3 trial outcomes.",
    "attendees": "Dr. Amit Sharma"
  }
}
```

### Supported Intents
- `log_interaction`
- `edit_interaction`
- `fetch_hcp_profile`
- `suggest_next_best_action`
- `schedule_followup`

---

## 🧪 Example Requests

### Log Interaction
```bash
curl -X POST http://127.0.0.1:8000/api/agent/chat \
-H "Content-Type: application/json" \
-d '{
  "intent":"log_interaction",
  "payload":{
    "hcp_id":1,
    "interaction_type":"Meeting",
    "interaction_date":"2026-04-17",
    "topics_discussed":"Discussed Product X efficacy in diabetic patients and shared positive trial outcomes.",
    "attendees":"Dr. Amit Sharma"
  }
}'
```

### Fetch HCP Profile
```bash
curl -X POST http://127.0.0.1:8000/api/agent/chat \
-H "Content-Type: application/json" \
-d '{
  "intent":"fetch_hcp_profile",
  "payload":{"hcp_id":1}
}'
```

### Suggest Next Best Action
```bash
curl -X POST http://127.0.0.1:8000/api/agent/chat \
-H "Content-Type: application/json" \
-d '{
  "intent":"suggest_next_best_action",
  "payload":{"sentiment":"positive"}
}'
```

### Schedule Follow-up
```bash
curl -X POST http://127.0.0.1:8000/api/agent/chat \
-H "Content-Type: application/json" \
-d '{
  "intent":"schedule_followup",
  "payload":{
    "interaction_id":1,
    "due_date":"2026-04-20",
    "owner":"Prateek",
    "note":"Share efficacy deck"
  }
}'
```

### Edit Interaction
```bash
curl -X POST http://127.0.0.1:8000/api/agent/chat \
-H "Content-Type: application/json" \
-d '{
  "intent":"edit_interaction",
  "payload":{
    "interaction_id":1,
    "updates":{"attendees":"Dr. Amit Sharma, Dr. Neha"}
  }
}'
```

---

## 🎥 Demo Walkthrough (Suggested)

1. Open frontend (`localhost:5173`)
2. Log an interaction
3. Show generated AI summary
4. Fetch HCP profile
5. Suggest next best action
6. Schedule a follow-up
7. Edit an existing interaction

---

## 📎 Validation & Data Notes

- `hcp_id` must reference an existing HCP record.
- Invalid `hcp_id` returns validation error.
- Demo uses seeded/hardcoded HCP records.

---

## 🧯 Troubleshooting

### 500 error while logging interaction
Possible cause: invalid foreign key (`hcp_id` not found in
