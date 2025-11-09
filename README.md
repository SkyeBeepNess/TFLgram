# Telegram TfL Bot 🚇

A simple Telegram bot built with **python-telegram-bot** that fetches live line status
data from the [TfL API](https://api.tfl.gov.uk).

## Features
- `/get_line_status` — Get the status of all Tube lines
- `/plan_journey <FROM_POSTCODE> <TO_POSTCODE>` — Creates a journey from <FROM_POSTCODE> to <TO_POSTCODE>

## Setup
```bash
git clone https://github.com/yourusername/telegram-tfl-bot.git
cd telegram-tfl-bot
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
echo BOT_TOKEN=your_token > .env
python main.py
