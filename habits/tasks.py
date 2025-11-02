from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.services import send_tg_message


@shared_task
def send_habits_notification():
    now = timezone.localtime()

    habits = Habit.objects.filter(
        time=now.replace(second=0, microsecond=0),
        is_pleasant_habit=False,
        user__tg_chat_id__isnull=False,
    )

    for habit in habits:
        try:
            message = (
                f"⏰ НАПОМИНАНИЕ: Я буду {habit.action} "
                f"в {habit.time.time()} {habit.place}"
            )
            send_tg_message(habit.user.tg_chat_id, message)

            habit.time = habit.time + timedelta(days=habit.periodicity)
            if habit.pleasant_habit:
                habit.pleasant_habit.time = habit.time
                habit.pleasant_habit.save()

            habit.save()

        except Exception as e:
            print(f"Не удалось отправить привычку {habit.action}: {e}")
