from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField


class CustomUser(AbstractUser):
    email = EmailField(unique=True, verbose_name='Email', help_text='Введите ваш email')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
