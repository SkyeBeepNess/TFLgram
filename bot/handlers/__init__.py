from telegram.ext import CommandHandler, MessageHandler, filters

from .start import start_command

def register_handlers(application):
    """Attach all handlers to the bot application."""
    application.add_handler(CommandHandler("start", start_command))
