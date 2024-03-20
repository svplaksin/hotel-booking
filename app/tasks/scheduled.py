import asyncio
from app.tasks.celery_app import celery
from app.tasks.reminders.bookings import booking_remind


@celery.task(name="email.booking_reminder_1day")
def remind_booking_1day():
    asyncio.run(booking_remind(1))


@celery.task(name="email.booking_reminder_3days")
def remind_booking_3days():
    asyncio.run(booking_remind(3))
