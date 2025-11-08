from telegram import Update
from telegram.ext import ContextTypes
from bot.services.tfl_api import get_line_status

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Hi {user.first_name or 'there'}! 👋\n"
        f"{get_line_status('tube')}"
    )