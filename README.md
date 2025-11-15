# MENA Career Insight API (Local LLM + Ollama + FastAPI)

This project is a local AI service that generates structured career insights and development plans for users in the MENA region.

It runs **fully locally** using:

- [Ollama](https://ollama.com) (with `llama3.2:3b` or another local model)
- [FastAPI](https://fastapi.tiangolo.com/)
- Python 3.10+

No external cloud API calls are used.

---

## Features

- Accepts a structured **user profile** (skills, education, interests, constraints).
- Returns a **MENA-focused career strategy** with:
  - `profileSnapshot`
  - `suggestedRoles`
  - `skillGapAnalysis`
  - `learningPlan` (3–6 month roadmap)
  - `jobSearchStrategy`
  - `constraintsNotes`
- Uses a local LLM through **Ollama’s HTTP API**.

---

## Project Structure

```text
career-insight-ollama/
├─ [main.py](http://_vscodecontentref_/0)                     # FastAPI app (endpoints + Ollama integration)
├─ requirements.txt            # Python dependencies
├─ [sample_request.json](http://_vscodecontentref_/1)         # Example request body
│
├─ models/
│  ├─ __init__.py
│  └─ schemas.py               # Pydantic models (UserProfile, CareerInsightsResponse, etc.)
│
└─ prompts/
   ├─ __init__.py
   └─ career_prompt.py         # SYSTEM_PROMPT + build_user_prompt


Prerequisites
Python 3.10+ installed

Ollama installed and running on your machine:

Download: https://ollama.com
Make sure you can run in your terminal:
ollama --version
ollama pull llama3.2:3b


git clone https://github.com/<your-username>/career-insight-ollama.git
cd career-insight-ollama


python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt


uvicorn main:app --reload --host 0.0.0.0 --port 8000

Usage (Swagger http://localhost:8000/docs) 
