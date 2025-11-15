"""Main orchestrator: wires agents together and runs a demo.
"""
import argparse
from agents.intake_agent import intake_message
from agents.interpretation_agent import interpret
from agents.risk_agent import detect_risks
from agents.loop_agent import run_feedback_loop
from agents.memory_agent import get_recent_history


def run_demo():
    print('Context Guardian — quick demo')
    print('Type a message you would send (empty to exit).')

    # show recent history
    hist = get_recent_history()
    if hist and isinstance(hist, dict):
        recent_list = hist.get("history", [])
        if recent_list:
            print('\nRecent corrections:')
            for h in recent_list:
                if isinstance(h, dict):
                    print('-', h.get('original'), '->', h.get('suggestion'))

    while True:
        msg = input('\nYour message: ').strip()
        if not msg:
            print('Exiting demo.')
            break

        packet = intake_message(msg)
        if 'run_demo_debug' in globals() and run_demo_debug:
            print("[DEBUG] Intake packet:", packet)

        interp = interpret(packet)
        if 'run_demo_debug' in globals() and run_demo_debug:
            print("[DEBUG] Interpretation object:", interp)

        risks = detect_risks(interp)
        if 'run_demo_debug' in globals() and run_demo_debug:
            print("[DEBUG] Risk analysis:", risks)

        result = run_feedback_loop(msg, risks)

        if 'run_json_mode' in globals() and run_json_mode:
            import json
            print(json.dumps({
                "input_message": msg,
                "interpretation": interp,
                "risks": risks,
                "output": result
            }, indent=2))
        else:
            print('\nFinal message:', result['final'])
            print('Status:', result['status'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug logs')
    parser.add_argument('-j', '--json', action='store_true', help='Print structured JSON output')
    parser.add_argument('-e', '--enable-llm', action='store_true', help='Enable LLM calls if LLM_API_KEY present')
    args = parser.parse_args()

    run_demo_debug = args.debug
    run_json_mode = args.json

    run_demo()
