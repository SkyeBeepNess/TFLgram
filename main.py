import logging

from telegram.ext import ApplicationBuilder

from bot.config import BOT_TOKEN
from bot.handlers import register_handlers


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register all handlers
    register_handlers(application)

    logger.info("Bot is starting…")
    application.run_polling()


if __name__ == "__main__":
    main()
