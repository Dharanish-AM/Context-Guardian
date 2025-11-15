"""A lightweight heuristics-based clarity scorer.

Scores messages on a scale 0..1 where lower means more ambiguous.
Also returns detected issues.
"""
import re
from typing import Tuple, List

AMBIGUITY_KEYWORDS = ["that", "this", "it", "soon", "later", "ASAP", "maybe", "some"]


def score_clarity(message: str) -> Tuple[float, List[str]]:
    issues = []
    score = 1.0

    # Too short
    if len(message.split()) < 3:
        issues.append('too_short')
        score -= 0.25

    # Ambiguous pronouns
    if any(re.search(r'\b' + re.escape(w) + r'\b', message, re.I) for w in AMBIGUITY_KEYWORDS):
        issues.append('ambiguous_references')
        score -= 0.2

    # Missing deadline / time
    if not re.search(r'\b(today|tomorrow|by \d{1,2}(:\d{2})? ?(am|pm)?|am|pm|\b\d{1,2}(:\d{2})?)\b', message, re.I):
        # not necessarily an issue but lower score
        issues.append('missing_deadline_hint')
        score -= 0.1

    # Missing recipient
    if not re.search(r'\b(to|@|please|could you|can you)\b', message, re.I):
        issues.append('missing_recipient_or_action')
        score -= 0.15

    # Clamp
    score = max(0.0, min(1.0, score))
    return score, issues
