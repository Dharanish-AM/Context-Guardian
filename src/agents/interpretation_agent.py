"""Interpretation Agent: extracts intent, action verbs, objects, and simple slots.
"""
import re
from typing import Dict


def interpret(message_packet: Dict) -> Dict:
    text = message_packet['raw']
    # Very simple heuristics
    verbs = re.findall(r"\b(send|deliver|review|check|finish|start|meet|call|email|submit|deploy|fix)\b", text, re.I)
    times = re.findall(r"\b(today|tomorrow|by \d{1,2}|\d{1,2}:\d{2}|am|pm)\b", text, re.I)
    recipients = re.findall(r"@\w+|to \w+|for \w+", text, re.I)

    return {
        'raw': text,
        'verbs': verbs,
        'times': times,
        'recipients': recipients,
        'notes': ''
    }
