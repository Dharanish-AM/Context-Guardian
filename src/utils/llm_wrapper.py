"""Simple LLM wrapper stub.

Replace `call_llm` with a real API call to OpenAI/Gemini if you want to use a hosted model.
If no API key is provided, a local heuristic fallback will be used by CorrectionAgent.
"""

import os
from dotenv import load_dotenv

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "").strip() or ""
if not LLM_PROVIDER:
    print("[ENV WARNING] LLM_PROVIDER not found in .env file")

LLM_API_KEY = os.getenv("LLM_API_KEY", "").strip() or ""
if not LLM_API_KEY:
    print("[ENV WARNING] LLM_API_KEY is missing or empty")


def call_llm(prompt: str, style: str = "neutral", max_tokens: int = 256) -> str:
    """
    Call Gemini 2.0 Pro with:
    - Style control: formal / friendly / brief / neutral
    - JSON structured response
    - Retry logic
    - Guardrails for safe fallback
    """
    if not LLM_API_KEY or LLM_PROVIDER.lower() != "gemini":
        print("[LLM WARNING] Using fallback: No valid Gemini configuration.")
        return ""

    import google.generativeai as genai

    genai.configure(api_key=LLM_API_KEY)

    # Choose model
    model = genai.GenerativeModel("gemini-2.0-flash")

    # Style prompt injection
    style_instructions = {
        "formal": "Rewrite the message in a clear, professional, formal tone.",
        "friendly": "Rewrite the message in a friendly, warm, casual tone.",
        "brief": "Rewrite the message in a very short, concise tone.",
        "neutral": "Rewrite the message in a neutral, clear tone.",
    }

    tone = style_instructions.get(style, style_instructions["neutral"])

    # Full structured prompt
    full_prompt = f"""
You are a communication-clarity agent.

STYLE: {style.upper()}
TASK: Rewrite the message with improved clarity, fixing ambiguity and adding placeholders if missing.
OUTPUT FORMAT: Return ONLY valid JSON in this structure:
{{
  "rewritten_text": "...",
  "reasoning": "...",
  "style_used": "{style}",
  "placeholders_added": true or false
}}

MESSAGE TO REWRITE:
{prompt}

INSTRUCTIONS:
- Do not hallucinate facts.
- Only add placeholders like [FILE_NAME], [DATE], [TIME].
- Keep meaning same.
- Ensure JSON is valid.
{tone}
"""

    # Retry logic (3 attempts)
    for attempt in range(3):
        try:
            response = model.generate_content(full_prompt)

            if hasattr(response, "text") and response.text.strip():
                return response.text.strip()

        except Exception as e:
            print(f"[LLM RETRY] Attempt {attempt+1} failed:", e)

    print("[LLM ERROR] All retries failed. Falling back to heuristic mode.")
    return ""
