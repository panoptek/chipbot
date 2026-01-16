from app.storage.base import Storage, UserProfile


class MemoryStorage(Storage):
    def __init__(self) -> None:
        self._users: dict[int, UserProfile] = {}

    def get_user(self, user_id: int) -> UserProfile | None:
        return self._users.get(user_id)

    def save_user(self, profile: UserProfile) -> None:
        self._users[profile.user_id] = profile
