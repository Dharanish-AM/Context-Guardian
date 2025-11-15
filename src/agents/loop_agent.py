"""Loop Agent: simple interactive loop to get user feedback and refine the suggestion.
"""
from typing import Dict
from agents.correction_agent import suggest_correction
from agents.memory_agent import store_correction


def run_feedback_loop(original: str, risks: Dict) -> Dict:
    """
    Improved loop agent with:
    - Style selection
    - Evaluation scoring
    - Smarter refinement flow
    """

    print("\nChoose rewrite style:")
    print("1. Formal\n2. Friendly\n3. Brief\n4. Neutral")
    style_choice = input("Select style [1-4]: ").strip()

    style_map = {
        "1": "formal",
        "2": "friendly",
        "3": "brief",
        "4": "neutral"
    }
    style = style_map.get(style_choice, "neutral")

    correction = suggest_correction(original, risks, style=style)

    print("\n--- Suggested message ---")
    print(correction["suggestion"])
    print("---")
    print(f"(Generated using style: {style})")

    # Evaluation scoring: ask user if message is clear
    clarity = input("\nRate clarity (1=bad, 5=excellent): ").strip()
    try:
        clarity_score = int(clarity)
    except:
        clarity_score = 3

    choice = input(
        "\nDo you want to (a)ccept, (e)dit, or (r)efine further? [a/e/r]: "
    ).strip().lower()

    if choice == "a":
        store_correction(original, correction["suggestion"])
        return {
            "final": correction["suggestion"],
            "status": "accepted",
            "clarity_score": clarity_score
        }

    elif choice == "e":
        edited = input("Paste your edited message: ").strip()
        store_correction(original, edited)
        return {
            "final": edited,
            "status": "edited",
            "clarity_score": clarity_score
        }

    else:
        # Improved refinement logic
        follow_up = input(
            "What should be improved? (tone, detail, placeholders, clarity): "
        ).strip()

        refined_prompt = (
            correction["suggestion"]
            + f"\nUser requested refinement: {follow_up}"
        )

        refined = suggest_correction(refined_prompt, risks, style=style)
        store_correction(original, refined["suggestion"])

        return {
            "final": refined["suggestion"],
            "status": "refined",
            "clarity_score": clarity_score,
            "refine_note": follow_up
        }
