from typing import Dict
from utils.llm_wrapper import call_llm
from agents.risk_agent import heuristic_rewrite

def suggest_correction(raw: str, risks: Dict, style: str = "neutral") -> Dict:
    """
    Suggest corrected message using:
    - LLM JSON structured rewrite (preferred)
    - Tone selection (formal/friendly/brief/neutral)
    - Safe fallback heuristic
    """

    prompt = f"{raw}"

    # Call LLM with structured JSON output
    llm_response = call_llm(prompt=prompt, style=style)

    suggestion = None
    reasoning = None
    placeholders = False

    # Attempt to parse JSON if present
    if llm_response:
        # Clean fenced code blocks like ```json ... ```
        cleaned = llm_response.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.strip("`").strip()
            if cleaned.lower().startswith("json"):
                cleaned = cleaned[4:].strip()
        llm_response = cleaned

        try:
            import json
            data = json.loads(llm_response)

            # Extract only rewritten_text
            rewritten = data.get("rewritten_text", "").strip()
            reasoning = data.get("reasoning", "")
            placeholders = data.get("placeholders_added", False)

            suggestion = rewritten

        except Exception:
            # JSON failed → treat raw text as rewrite if any
            if llm_response and isinstance(llm_response, str):
                suggestion = llm_response.strip()

    # If still no valid suggestion → fallback
    if not suggestion:
        suggestion = heuristic_rewrite(raw, risks.get("issues", []))
        used = "heuristic"
    else:
        used = "llm"

    return {
        "original": raw,
        "suggestion": suggestion,
        "style_used": style,
        "reasoning": reasoning,
        "placeholders_added": placeholders,
        "used": used
    }
