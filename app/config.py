import os


def _split_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


BOT_NAME = os.getenv("BOT_NAME", "Чип")
BOT_ALIASES = _split_csv(os.getenv("BOT_ALIASES", "chip,чип"))
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

OWNER_USER_ID = int(os.getenv("OWNER_USER_ID", "0"))
DAILY_USER_LIMIT = int(os.getenv("DAILY_USER_LIMIT", "30"))

SYSTEM_PROMPT = (
    "Ты — Чип, весёлый и дружелюбный чат-бот. "
    "Отвечай кратко, дружелюбно и по делу. "
    "Всегда отвечай на том языке, на котором написан последний вопрос пользователя."
)
