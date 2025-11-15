"""Memory Agent: stores and retrieves simple user preferences and past corrections.

For simplicity this uses a JSON file as a memory bank.
"""
import json
from pathlib import Path
from typing import Dict

MEMORY_FILE = Path(__file__).parent.parent / 'memory_bank.json'


def _read_memory() -> Dict:
    if not MEMORY_FILE.exists():
        return {}
    try:
        return json.loads(MEMORY_FILE.read_text())
    except Exception:
        return {}


def _write_memory(mem: Dict):
    MEMORY_FILE.write_text(json.dumps(mem, indent=2))


def store_correction(original: str, suggestion: str, style: str = "neutral", clarity_score: int = None):
    mem = _read_memory()

    history = mem.get('history', [])
    history.append({
        'original': original,
        'suggestion': suggestion,
        'style_used': style,
        'clarity_score': clarity_score,
        'timestamp': __import__('datetime').datetime.now().isoformat()
    })
    mem['history'] = history[-200:]  # keep last 200 items

    # Update style preference scoring
    prefs = mem.get('style_preferences', {})
    prefs[style] = prefs.get(style, 0) + 1
    mem['style_preferences'] = prefs

    _write_memory(mem)


def get_recent_history(limit: int = 5):
    mem = _read_memory()
    return {
        "history": mem.get('history', [])[-limit:],
        "style_preferences": mem.get('style_preferences', {})
    }
