# AI CRM HCP Assistant

AI-powered CRM assistant for managing **HCP (Healthcare Professional)** interactions, generating intelligent summaries, and recommending next actions.

---

## Overview

This project streamlines field-force and medical-rep workflows by combining a structured CRM backend with an AI-powered agent layer.

### Core Capabilities
- Log HCP interactions
- Generate AI summaries from interaction notes (Groq LLM)
- Edit interaction records
- Fetch HCP profile details
- Suggest next best actions
- Schedule follow-up tasks

---

## Tech Stack

### Backend
- **FastAPI** (API framework)
- **SQLAlchemy** (ORM)
- **PostgreSQL / SQLite** (database, based on your config)
- **LangChain + Groq** (LLM integration)

### Frontend
- **React (Vite)**
- **Axios**

---

## Architecture

```text
Frontend (React)
   ↓ HTTP
FastAPI API Layer (/api/agent/chat)
   ↓
Intent Router (agent.py)
   ↓
Tool Handlers (log_interaction, fetch_hcp, suggest_nba, etc.)
   ↓
SQLAlchemy Models + DB
   ↓
LLM Service (Groq via LangChain) for summarization/recommendations
```

---

## Repository Structure

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

## Features

### 1) Log Interaction
Creates a new interaction for an existing HCP and generates a concise AI summary.

### 2) Fetch HCP Profile
Retrieves profile details using `hcp_id`.

### 3) Suggest Next Best Action
Returns contextual recommendations based on interaction context/sentiment.

### 4) Schedule Follow-up
Creates a follow-up task linked to an interaction.

### 5) Edit Interaction
Updates selected fields of an existing interaction record.

---

## Prerequisites

- Python 3.10+
- Node.js 18+
- npm
- Valid Groq API key

---

## Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create `backend/.env`:

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

Run backend:

```bash
uvicorn app.main:app --reload --port 8000
```

Backend URLs:
- API: `http://127.0.0.1:8000`
- Swagger: `http://127.0.0.1:8000/docs`

---

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend URL:
- `http://localhost:5173`

---

## API Contract

### Endpoint
`POST /api/agent/chat`

### Request Body
```json
{
  "intent": "log_interaction",
  "payload": {
    "hcp_id": 1,
    "interaction_type": "Meeting",
    "interaction_date": "2026-04-15",
    "topics_discussed": "Discussed Product X efficacy...",
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

## Example Requests

### Log Interaction
```bash
curl -X POST http://127.0.0.1:8000/api/agent/chat \
-H "Content-Type: application/json" \
-d '{
  "intent":"log_interaction",
  "payload":{
    "hcp_id":1,
    "interaction_type":"Meeting",
    "interaction_date":"2026-04-15",
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

## Demo Walkthrough (Suggested)

1. Open frontend (`localhost:5173`)
2. Log an interaction
3. Show generated AI summary
4. Fetch HCP profile
5. Suggest next best action
6. Schedule a follow-up
7. Edit an existing interaction

---

## Validation & Data Notes

- `hcp_id` must reference an existing HCP record.
- If `hcp_id` does not exist, interaction creation should fail with a clear validation error.
- Keep seeded/hardcoded HCP records for demo unless HCP CRUD is explicitly required.

---

## Troubleshooting

### 500 error while logging interaction
Possible cause: invalid foreign key (`hcp_id` not found in `hcp` table).

Fix:
- Use an existing HCP ID, or
- Seed/create that HCP first.

### LLM not generating output
- Verify `GROQ_API_KEY` in `backend/.env`
- Restart backend after `.env` changes
- Confirm selected model is available for your account

### CORS/Frontend connection issue
- Ensure backend is running on `http://127.0.0.1:8000`
- Ensure frontend API base URL matches backend port

---

## Security & Git Hygiene

Add these to `.gitignore` (backend/frontend as applicable):
- `.env`
- `.venv/`
- `node_modules/`
- local DB files (`*.db`) if used

Never commit secrets (API keys, tokens, credentials).

---

## Future Improvements

- HCP master CRUD module
- Auth + role-based access
- Interaction timeline view
- Advanced analytics dashboard
- Unit/integration tests and CI pipeline

---

## Author

**Prateek**