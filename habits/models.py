from django.db import models
from django.db.models import BooleanField, CharField, DateTimeField, ForeignKey, PositiveIntegerField

from users.models import CustomUser


class Habit(models.Model):
    user = ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    place = CharField(
        max_length=100,
        verbose_name="Место выполнения",
        help_text="Укажите место выполнения",
    )
    time = DateTimeField(
        verbose_name="Время следующего выполнения",
        help_text="Дата и время следующего выполнения (в формате YYYY-MM-DD HH:MM:SS",
    )
    action = CharField(
        max_length=300,
        verbose_name="Действие",
        help_text="Укажите действие - саму привычку",
    )
    is_pleasant_habit = models.BooleanField(
        default=False, verbose_name="Признак приятной привычки"
    )
    pleasant_habit = models.ForeignKey(
        "Habit",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Приятная привычка",
        help_text="Связанная приятная привычка (только для полезных привычек)",
    )
    periodicity = PositiveIntegerField(
        default=7,
        verbose_name="Периодичность выполнения",
        help_text="Добавьте периодичность выполнения в днях (по умолчанию ежедневно)",
    )
    reward = CharField(
        max_length=300,
        verbose_name="Вознаграждение",
        null=True,
        blank=True,
        help_text="Вознаграждение за выполнение полезной привычки",
    )
    time_to_do = PositiveIntegerField(
        verbose_name="Время на выполнение",
        help_text="Добавьте время на выполнение в секундах",
    )
    is_public = BooleanField(
        default=False,
        verbose_name="Признак публичности",
        help_text="Определите, будет ли публикация публичной",
    )

    def __str__(self):
        return f"Привычка {self.action}"

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"

        constraints = [
            models.UniqueConstraint(
                fields=["user", "place", "time", "action"], name="unique_habit_for_user"
            )
        ]
