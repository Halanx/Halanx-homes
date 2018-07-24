from datetime import datetime

from django.utils import timezone


def get_datetime(raw_date):
    return timezone.make_aware(datetime.strptime(raw_date, "%Y-%m-%d"), timezone.get_default_timezone())
