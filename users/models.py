from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email обязателен")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = EmailField(unique=True, verbose_name="Email", help_text="Введите ваш email")
    username = CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name="Username",
        help_text="Введите ваш username",
    )

    objects = CustomUserManager()
    tg_chat_id = CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Телеграмм чат id",
        help_text="Укажите телеграмм чат id",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
