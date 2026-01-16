from telegram import Update
from telegram.ext import ContextTypes

from app.bot.limits import RateLimiter
from app.bot.mention import is_mentioned
from app.config import BOT_ALIASES, BOT_NAME
from app.services.openai_client import OpenAIService
from app.storage.base import UserProfile
from app.storage.memory import MemoryStorage


class BotHandlers:
    def __init__(self, limiter: RateLimiter) -> None:
        self._limiter = limiter
        self._openai = OpenAIService()
        self._storage = MemoryStorage()

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        message = update.message
        if message is None or message.text is None:
            return

        chat_type = message.chat.type
        text = message.text.strip()

        if chat_type != "private" and not is_mentioned(text, BOT_NAME, BOT_ALIASES):
            return

        user = message.from_user
        if user:
            profile = UserProfile(user_id=user.id, username=user.username, language=user.language_code)
            self._storage.save_user(profile)

        user_id = user.id if user else None
        if not self._limiter.can_use(user_id):
            remaining = self._limiter.remaining(user_id)
            await message.reply_text(
                "Лимит сообщений на сегодня исчерпан. "
                + (f"Осталось: {remaining}." if remaining is not None else "")
            )
            return

        reply = self._openai.generate_reply(text)
        await message.reply_text(reply)
        self._limiter.record_use(user_id)
