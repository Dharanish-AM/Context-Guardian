"""Risk Detection Agent: identifies communication risks based on interpretation and clarity scorer.
"""
from typing import Dict
from tools.clarity_scorer import score_clarity


def detect_risks(interpretation: Dict) -> Dict:
    """
    Enhanced risk detection:
    - Additional ambiguity checks
    - Missing subject, missing action, missing context
    - Severity scoring
    """
    raw = interpretation.get('raw', '')
    score, issues = score_clarity(raw)

    extra_flags = []

    # Missing verb check
    if not interpretation.get('verbs'):
        extra_flags.append("missing_action")

    # Missing recipient check
    if not interpretation.get('recipients'):
        extra_flags.append("missing_recipient")

    # Missing time/date
    if not interpretation.get('times'):
        extra_flags.append("missing_time")

    # Extremely short message
    if len(raw.strip().split()) <= 2:
        extra_flags.append("too_short_message")

    # Context ambiguity (checking if message is vague)
    vague_terms = ["stuff", "things", "that thing", "the thing", "do it", "handle it"]
    if any(v in raw.lower() for v in vague_terms):
        extra_flags.append("vague_context")

    # Build full risk dictionary
    risks = {
        "clarity_score": score,
        "issues": issues,
        "extra_flags": extra_flags,
    }

    # Derived severity
    severity = "low"
    if score < 0.3 or "missing_action" in extra_flags:
        severity = "high"
    elif score < 0.6 or "vague_context" in extra_flags:
        severity = "medium"

    risks["severity"] = severity
    return risks


# Minimal fallback rewrite used when LLM fails.
def heuristic_rewrite(raw: str, issues: list) -> str:
    """
    Minimal fallback rewrite used when LLM fails.
    Improves clarity by adding placeholders and structure.
    """
    text = raw.strip()

    if "missing_action" in issues or "missing_recipient" in issues:
        text = f"Please specify the recipient and action: '{raw}'"

    if "missing_time" in issues:
        text += " (add expected date/time)"

    if "too_short_message" in issues:
        text = f"Message is unclear: '{raw}'. Please provide more detail."

    if "vague_context" in issues:
        text = f"Your message is vague: '{raw}'. Specify what exactly is needed."

    # Generic fallback if nothing matches
    if text == raw.strip():
        text = f"Please clarify your message: '{raw}'"

    return text
