import logging

from telegram.ext import ApplicationBuilder, MessageHandler, filters

from app.bot.handlers import BotHandlers
from app.bot.limits import RateLimiter
from app.config import DAILY_USER_LIMIT, OWNER_USER_ID, TELEGRAM_BOT_TOKEN

logging.basicConfig(level=logging.INFO)


def build_app() -> None:
    limiter = RateLimiter(daily_limit=DAILY_USER_LIMIT, owner_user_id=OWNER_USER_ID)
    handlers = BotHandlers(limiter)

    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.handle_message))

    app.run_polling()


if __name__ == "__main__":
    if not TELEGRAM_BOT_TOKEN:
        raise SystemExit("TELEGRAM_BOT_TOKEN is required")
    build_app()
