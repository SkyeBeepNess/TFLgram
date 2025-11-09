from telegram.ext import CommandHandler, MessageHandler, filters

from .get_line_status import get_line_status_command
from .plan_journey import plan_journey_command

def register_handlers(application):
    """Attach all handlers to the bot application."""
    application.add_handler(CommandHandler("get_line_status", get_line_status_command))
    application.add_handler(CommandHandler("plan_journey", plan_journey_command))
