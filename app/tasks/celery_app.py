from celery import Celery
from celery.schedules import crontab

from app.config import settings

celery = Celery(
    "tasks",
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
    include=[
        "app.tasks.tasks",
        "app.tasks.scheduled"
    ]
)

celery.conf.beat_schedule = {
    "remind_1day": {
        "task": "booking_reminder_1day",
        "schedule": crontab(minute="0", hour="9"),
    },
    "remind_3days": {
        "task": "booking_reminder_3days",
        "schedule": crontab(minute="30", hour="15")
    }
}
