"""Intake Agent: collects the user's raw message and metadata.
"""
from typing import Dict


def intake_message(user_message: str, metadata: Dict = None) -> Dict:
    metadata = metadata or {}
    return {
        'raw': user_message.strip(),
        'metadata': metadata
    }
