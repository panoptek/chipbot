import re
import unicodedata


def _normalize(text: str) -> str:
    return unicodedata.normalize("NFKC", text).casefold()


def is_mentioned(text: str, bot_name: str, aliases: list[str]) -> bool:
    if not text:
        return False

    normalized = _normalize(text)
    candidates = [bot_name, *aliases]
    for candidate in candidates:
        if not candidate:
            continue
        token = re.escape(_normalize(candidate))
        if re.search(rf"\b{token}\b", normalized):
            return True
    return False
