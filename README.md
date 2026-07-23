# AI-First CRM HCP Module

An AI-powered Customer Relationship Management (CRM) module designed for Healthcare Professionals (HCPs). This application enables pharmaceutical sales representatives to log and manage doctor interactions through either a traditional form or a conversational AI assistant.

The project follows an AI-first architecture where LangGraph orchestrates an LLM-powered workflow to extract structured information, summarize conversations, and maintain interaction records.

---

# Features

## HCP Management
- View available Healthcare Professionals
- Select an HCP before logging interactions

## Log Interaction

Supports two methods:

### 1. Traditional Form
Sales representatives can manually enter:

- Interaction Type
- Date
- Time
- Attendees
- Topics Discussed
- Materials Shared
- Samples Distributed
- Sentiment
- Outcomes
- Follow-up Actions

### 2. Conversational AI

Users can simply chat naturally.

Example:

> Met Dr. Rahul yesterday afternoon. We discussed GlucoCare XR clinical trial results. He liked the efficacy data and requested additional sample packs next week.

The AI automatically extracts structured fields and updates the form.

---

# Edit Existing Interaction

Existing interactions can be modified through AI chat.

Example:

> Actually remove the sample distribution and change the sentiment to Neutral.

Only the requested fields are updated while preserving existing information.

---

# AI Workflow

The project uses LangGraph to orchestrate multiple AI nodes.

Workflow:

START
↓

Extract Information

↓

Resolve HCP

↓

Determine Intent

├── Log Interaction

└── Edit Interaction

↓

Generate Summary

↓

Return Response

END

---

# LangGraph Tools

The AI Agent uses multiple tools:

### 1. Extract Tool

Extracts structured information from natural language.

Outputs:

- interaction type
- date
- time
- attendees
- topics discussed
- materials shared
- samples distributed
- outcomes
- follow-up actions
- sentiment

---

### 2. Resolve HCP Tool

Matches the selected HCP with the doctor's name mentioned in chat.

Detects conflicts between selected HCP and extracted HCP.

---

### 3. Log Interaction Tool

Creates a new interaction in PostgreSQL.

---

### 4. Edit Interaction Tool

Updates an existing interaction while preserving unchanged fields.

---

### 5. Summarize Tool

Generates a concise meeting summary using the LLM.

---

# Tech Stack

## Frontend

- React
- Redux Toolkit
- Axios
- Tailwind CSS
- Vite

## Backend

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic

## AI

- LangGraph
- Groq API
- gemma2-9b-it

## Database

- PostgreSQL

---

# Project Structure

```
crm-hcp/
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── app/
│   │   ├── components/
│   │   ├── features/
│   │   ├── pages/
│   │   └── styles/
│   │
│   ├── package.json
│   └── vite.config.js
│
├── backend/
│   ├── app/
│   │
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── graph/
│   ├── llm/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── tools/
│   ├── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/crm-hcp.git

cd crm-hcp
```

---

# Backend Setup

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
cd backend

pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file inside the backend folder.

Example:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/crm_hcp

GROQ_API_KEY=your_groq_api_key
```

---

## Run Backend

```bash
uvicorn app.main:app --reload
```

Backend:

```
http://localhost:8000
```

Swagger Documentation:

```
http://localhost:8000/docs
```

---

# Frontend Setup

Open another terminal.

```bash
cd frontend

npm install
```

Run:

```bash
npm run dev
```

Frontend:

```
http://localhost:5173
```

---

# API Endpoints

## HCP APIs

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | /hcps | Get all HCPs |
| POST | /hcps | Create HCP |

---

## Interaction APIs

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | /interactions | Get interactions |
| POST | /interactions | Create interaction |
| PUT | /interactions/{id} | Update interaction |

---

## AI Agent

| Method | Endpoint |
|----------|-----------|
| POST | /agent/chat |

Example Request

```json
{
  "hcp_id": 1,
  "interaction_id": null,
  "message": "Met Dr Rahul today. Discussed GlucoCare XR."
}
```

---

# AI Conversation Examples

## Log Interaction

Input

```
Met Dr Rahul today.

Discussed GlucoCare XR.

Shared product brochure.

Doctor requested more samples next week.
```

Output

- Structured interaction
- AI generated summary
- Stored in PostgreSQL

---

## Edit Interaction

Input

```
Change sentiment to Neutral.

Remove samples distributed.
```

Output

Only modified fields are updated.

---

# Future Improvements

- Voice-to-text interaction logging
- OCR support for handwritten notes
- Meeting transcription
- Calendar integration
- Reminder notifications
- Analytics Dashboard
- Multi-user authentication
- Role-based access control

---

# Assignment Requirements Covered

- React Frontend
- Redux State Management
- FastAPI Backend
- LangGraph Agent
- Groq LLM
- gemma2-9b-it Model
- PostgreSQL Database
- AI-assisted Logging
- AI-assisted Editing
- LangGraph Tools
- GitHub Repository
- REST APIs

---

# Author

**Prajwal Patil**

Bachelor of Engineering (Computer Science)

Built as part of the AI-First CRM HCP Module assignment.