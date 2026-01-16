from __future__ import annotations

from dataclasses import dataclass


@dataclass
class UserProfile:
    user_id: int
    username: str | None
    language: str | None = None


class Storage:
    """Interface placeholder for future database-backed storage."""

    def get_user(self, user_id: int) -> UserProfile | None:
        raise NotImplementedError

    def save_user(self, profile: UserProfile) -> None:
        raise NotImplementedError
