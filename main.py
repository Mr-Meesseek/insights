import json
import json5
import subprocess
from typing import Any, Dict
import requests

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models.schemas import UserProfile, CareerInsightsResponse
from prompts.career_prompt import SYSTEM_PROMPT, build_user_prompt

app = FastAPI(
    title="MENA Career Insight API",
    description="Local career insights powered by Ollama + LLM",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def call_ollama(model: str, system_prompt: str, user_prompt: str) -> str:
    """
    Call the local Ollama HTTP API and return the full response text.
    """
    url = "http://127.0.0.1:11434/api/generate"

    prompt = f"<<SYS>>\n{system_prompt}\n<</SYS>>\n\n{user_prompt}"

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False  # single JSON response
    }

    try:
        resp = requests.post(url, json=payload)
        resp.raise_for_status()
    except Exception as e:
        raise RuntimeError(f"Ollama HTTP error: {e}")

    data = resp.json()
    text = data.get("response", "") or ""
    return text.strip()

def extract_json(text: str) -> str:
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("No JSON object found in text")
    return text[start : end + 1]


@app.post("/career-insights", response_model=CareerInsightsResponse)
def generate_career_insights(profile: UserProfile):
    try:
        user_prompt = build_user_prompt(profile)

        raw_output = call_ollama(
            model="llama3.2:3b",
            system_prompt=SYSTEM_PROMPT,
            user_prompt=user_prompt,
        )

        print("RAW OUTPUT FROM MODEL:")
        print(raw_output)

        # First, extract JSON part
        json_text = extract_json(raw_output)

        # Try strict json first
        try:
            parsed: Dict[str, Any] = json.loads(json_text)
        except json.JSONDecodeError:
            # Fallback: use json5 to tolerate minor issues like missing commas
            parsed = json5.loads(json_text)

        return CareerInsightsResponse(**parsed)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}