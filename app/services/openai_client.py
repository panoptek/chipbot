from openai import OpenAI

from app.config import OPENAI_API_KEY, OPENAI_MODEL, SYSTEM_PROMPT


class OpenAIService:
    def __init__(self) -> None:
        self._client = OpenAI(api_key=OPENAI_API_KEY)

    def generate_reply(self, user_text: str) -> str:
        response = self._client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text},
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
