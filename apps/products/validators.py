from django.core.exceptions import ValidationError
from datetime import datetime
from zoneinfo import ZoneInfo

from core.settings import base

now = datetime.now(tz=ZoneInfo(f"{base.TIME_ZONE}"))


def validate_rebate_time(value):
    if value.until_time <= now:
        print('aaa')
        raise ValidationError(
            "Error"
        )
