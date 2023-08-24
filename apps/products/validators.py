from django.core.exceptions import ValidationError
from datetime import datetime
from zoneinfo import ZoneInfo

from core.settings import base

now = datetime.now(tz=ZoneInfo(f"{base.TIME_ZONE}"))


def validate_rebate_time(value):
    if value <= now:
        raise ValidationError(
            "Until time must be greater than current time"
        )
