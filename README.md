# Context Guardian — AI Agent for Clear Communication

Context Guardian is a multi-agent system that rewrites unclear human messages into clear, actionable communication using Gemini 2.0 Flash.

This project is built for the Kaggle Agents Intensive Capstone (Enterprise Track).

## Features
- Multi-agent architecture
- Ambiguity & clarity risk analysis
- Style-controlled LLM rewriting
- Memory-based personalization
- Refinement feedback loop
- JSON structured LLM responses
- Reliable guardrails & retries
- CLI & Notebook demos

## Run
python src/main.py

## Flags
--debug   detailed logs
--json    structured output
--enable-llm  use Gemini API

## Architecture
Intake → Interpretation → Risk → Correction (LLM) → Loop → Memory

## Ideal for
- Workplace communication
- Support teams
- Messaging automations

PRs welcome!
