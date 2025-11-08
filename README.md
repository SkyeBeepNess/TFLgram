# Telegram TfL Bot 🚇

A simple Telegram bot built with **python-telegram-bot** that fetches live line status
data from the [TfL API](https://api.tfl.gov.uk).

## Features
- `/start` — get status for Tube

## Setup
```bash
git clone https://github.com/yourusername/telegram-tfl-bot.git
cd telegram-tfl-bot
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
echo BOT_TOKEN=your_token > .env
python main.py
