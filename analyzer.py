"""
analyzer.py — Backend logic for legal document risk analysis.
Handles PDF text extraction and LLM API calls via Groq.
Returns a clean dictionary with risk_score, red_flags, and summary.

API key resolution order:
  1. st.secrets["GROQ_API_KEY"]  (Streamlit Cloud deployment)
  2. GROQ_API_KEY env var         (local .env via python-dotenv)
"""

import io
import json
import os
import ollama

from pypdf import PdfReader
from groq import Groq
from dotenv import load_dotenv

# Load .env when running locally (no-op if already set or on Streamlit Cloud)
load_dotenv()


# ── API key helper ─────────────────────────────────────────────────────────────

def get_api_key() -> str:
    """
    Return the Groq API key.
    Tries Streamlit secrets first, falls back to environment variable.
    Raises RuntimeError if neither is available.
    """
    # Try Streamlit secrets (works on Streamlit Cloud and locally via secrets.toml)
    try:
        import streamlit as st
        key = st.secrets.get("GROQ_API_KEY", "")
        if key:
            return key
    except Exception:
        pass

    # Fall back to environment variable (local .env)
    key = os.getenv("GROQ_API_KEY", "")
    if key:
        return key

    raise RuntimeError(
        "GROQ_API_KEY not found. "
        "Add it to .streamlit/secrets.toml (local) or Streamlit Cloud secrets."
    )


# ── Prompt ────────────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are an expert legal document analyst specializing in risk assessment.
Analyze the provided legal document text and identify potential risks, red flags, and concerns.

You MUST respond with ONLY valid JSON in this exact format (no markdown, no extra text):
{
  "risk_score": <integer 0-100>,
  "red_flags": [
    "<concise description of risk 1>",
    "<concise description of risk 2>"
  ],
  "summary": "<2-3 sentence plain-English summary of the document and its overall risk level>"
}

Risk score guide:
  0–25  → Low risk
  26–50 → Moderate risk
  51–75 → High risk
  76–100 → Critical risk

Be specific. Cite clause types (e.g. indemnification, non-compete, auto-renewal) when flagging risks."""


# ── PDF extraction ─────────────────────────────────────────────────────────────

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract all text from a PDF given its raw bytes."""
    reader = PdfReader(io.BytesIO(file_bytes))
    pages_text = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages_text.append(text)
    return "\n\n".join(pages_text)


# ── LLM call ──────────────────────────────────────────────────────────────────

def analyze_document(file_bytes: bytes) -> dict:
    """
    Main entry point.

    Args:
        file_bytes: Raw bytes of the uploaded PDF.

    Returns:
        dict with keys: risk_score (int), red_flags (list[str]), summary (str)

    Raises:
        ValueError:   If text extraction fails or the LLM returns malformed JSON.
        RuntimeError: If the API key is missing.
        Exception:    Propagates Groq API errors as-is.
    """
    api_key = get_api_key()

    # 1. Extract text
    document_text = extract_text_from_pdf(file_bytes)
    if not document_text.strip():
        raise ValueError(
            "Could not extract any text from this PDF. "
            "It may be scanned or image-based."
        )

    # Truncate to avoid token limits (~12 000 words ≈ 16 000 tokens)
    max_chars = 48_000
    if len(document_text) > max_chars:
        document_text = document_text[:max_chars] + "\n\n[Document truncated for analysis]"

    # 2. Call Groq
    client = Groq(api_key=api_key)
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    "Please analyze the following legal document and return "
                    "the JSON risk assessment:\n\n"
                    f"{document_text}"
                ),
            },
        ],
        temperature=0.1,
        max_tokens=1_024,
        response_format={"type": "json_object"},
    )

    raw_response = chat_completion.choices[0].message.content

    # 3. Parse & validate
    try:
        result = json.loads(raw_response)
    except json.JSONDecodeError as exc:
        raise ValueError(f"LLM returned invalid JSON: {exc}\n\nRaw: {raw_response}") from exc

    # Normalise types defensively
    result["risk_score"] = int(result.get("risk_score", 0))
    result["red_flags"]  = list(result.get("red_flags", []))
    result["summary"]    = str(result.get("summary", "No summary provided."))

    return result

def analyze_document_ollama(
    file_bytes: bytes,
    model: str = "llama3.2"
):
    document_text = extract_text_from_pdf(file_bytes)

    if not document_text.strip():
        raise ValueError(
            "Could not extract any text from this PDF."
        )

    response = ollama.chat(
    model=model,
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": (
                "Please analyze the following legal document "
                "and return ONLY JSON:\n\n"
                + document_text[:48000]
            )
        }
    ],
    format="json",
    options={
        "num_predict": 2048
    }
)

    raw_response = response["message"]["content"]

    result = json.loads(raw_response)

    return {
        "risk_score": int(result.get("risk_score", 0)),
        "red_flags": list(result.get("red_flags", [])),
        "summary": str(result.get("summary", ""))
    }
