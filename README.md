# Day 7 — AI Portfolio Generator

> An AI that builds your portfolio website for you — built as Day 7 of my AI Enablement portfolio.

## What This Does
Describe your 7 projects in Python, run the script, and GPT-4o-mini generates a complete, styled HTML portfolio site automatically.

## Why I Built It
To close out 7 days of AI projects with something meta — an AI that showcases all the other AIs I built.

## How It Works
1. Projects are defined in `generator.py`
2. GPT-4o-mini receives them as a prompt
3. It returns a complete HTML page with dark theme, project cards, and skills section
4. The HTML is saved to `portfolio.html` — open it in any browser

## Tech Stack
- Python 3
- OpenAI API (GPT-4o-mini)
- python-dotenv

## How to Run
1. Clone the repo
2. `pip3 install openai python-dotenv`
3. Copy `.env.example` to `.env` and add your OpenAI API key
4. `python3 generator.py`
5. Open `portfolio.html` in your browser

## Result
A fully generated dark-themed portfolio site — created entirely by AI.
