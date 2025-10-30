from django import forms
from django.db import models
from django.db.models import ForeignKey, CharField, TimeField, PositiveIntegerField, BooleanField

from users.models import CustomUser


class Habit(models.Model):
    user = ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    place = CharField(max_length=100, verbose_name='Место выполнения', help_text='Укажите место выполнения')
    time = TimeField(verbose_name='Время выполнения', help_text='Укажите время выполнения')
    action = CharField(max_length=300, verbose_name='Действие', help_text='Укажите действие - саму привычку')
    is_pleasant_habit = models.BooleanField(default=False, verbose_name="Признак приятной привычки")
    pleasant_habit = models.ForeignKey('Habit', on_delete=models.SET_NULL, null=True, blank=True,
                                       verbose_name='Приятная привычка',
                                       help_text='Связанная приятная привычка (только для полезных привычек)')
    periodicity = PositiveIntegerField(default=1, verbose_name='Периодичность выполнения',
                                       help_text='Добавьте периодичность выполнения в днях (по умолчанию ежедневно)')
    reward = CharField(max_length=300, verbose_name='Вознаграждение',
                       help_text='Вознаграждение за выполнение полезной привычки')
    time_to_do = PositiveIntegerField(verbose_name='Время на выполнение', help_text='Добавьте время на выполнение')
    is_public = BooleanField(default=False, verbose_name='Признак публичности',
                             help_text='Определите, будет ли публикация публичной')

    def __str__(self):
        return f'Привычка {self.action}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('time').formfield.widget = forms.TimeInput(
            format='%H:%M',
            attrs={'type': 'time'}
        )
