from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class UsageRecord:
    date: str
    count: int = 0


class RateLimiter:
    def __init__(self, daily_limit: int, owner_user_id: int) -> None:
        self.daily_limit = daily_limit
        self.owner_user_id = owner_user_id
        self._usage: dict[int, UsageRecord] = {}

    def _today(self) -> str:
        return datetime.now(timezone.utc).date().isoformat()

    def can_use(self, user_id: int | None) -> bool:
        if not user_id:
            return False
        if user_id == self.owner_user_id:
            return True
        record = self._get_record(user_id)
        return record.count < self.daily_limit

    def record_use(self, user_id: int | None) -> None:
        if not user_id or user_id == self.owner_user_id:
            return
        record = self._get_record(user_id)
        record.count += 1

    def remaining(self, user_id: int | None) -> int | None:
        if not user_id:
            return None
        if user_id == self.owner_user_id:
            return None
        record = self._get_record(user_id)
        return max(self.daily_limit - record.count, 0)

    def _get_record(self, user_id: int) -> UsageRecord:
        today = self._today()
        record = self._usage.get(user_id)
        if record is None or record.date != today:
            record = UsageRecord(date=today, count=0)
            self._usage[user_id] = record
        return record
