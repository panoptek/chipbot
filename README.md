# chipbot

Базовый каркас для чат-бота «Чип» с интеграцией OpenAI API и Telegram.

## Возможности
- Ответы в личных сообщениях и в группах по упоминанию имени (без учета регистра). Имя и псевдонимы настраиваются.
- Ответ всегда на языке пользователя (задается системным промптом).
- Базовые дневные лимиты запросов с исключением для владельца.
- Заготовка под будущую БД (интерфейс хранилища и память по умолчанию).

## Быстрый старт

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Создайте переменные окружения:

```bash
export TELEGRAM_BOT_TOKEN="..."
export OPENAI_API_KEY="..."
export BOT_NAME="Чип"
export BOT_ALIASES="chip,чип"
export OWNER_USER_ID="123456789"
export DAILY_USER_LIMIT="30"
export OPENAI_MODEL="gpt-4o-mini"
```

Запуск:

```bash
python -m app.main
```

## Где расширять
- `app/storage` — подключить базу данных для контекстов, фактов и профилей.
- `app/bot/limits.py` — заменить in-memory лимиты на постоянное хранилище.
- `app/bot/mention.py` — расширить правила упоминания, добавить сленг и дополнительные языки.
