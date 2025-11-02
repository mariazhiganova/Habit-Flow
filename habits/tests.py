from datetime import timedelta

from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import CustomUser


class HabitsTEstCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email="testuser@mail.com", password="testuser123"
        )
        self.user_2 = CustomUser.objects.create_user(
            email="testuser2@mail.com", password="testuser1232"
        )

        self.existing_habit_1 = Habit.objects.create(
            user=self.user,
            place="Дома",
            time=timezone.now() + timedelta(days=1),
            action="Делать 10 раз пресс",
            is_pleasant_habit=False,
            periodicity=1,
            reward="Съесть шоколадку",
            time_to_do=60,
            is_public=True,
        )
        self.existing_habit_2 = Habit.objects.create(
            user=self.user,
            place="Дома",
            time=timezone.now() + timedelta(days=1),
            action="Выходить на прогулку",
            is_pleasant_habit=True,
            periodicity=1,
            time_to_do=60,
            is_public=True,
        )

        self.existing_habit_3 = Habit.objects.create(
            user=self.user,
            place="Дома",
            time=timezone.now() + timedelta(days=1),
            action="Читать 10 страниц книги",
            pleasant_habit=self.existing_habit_2,
            is_pleasant_habit=False,
            periodicity=1,
            time_to_do=60,
            is_public=True,
        )

        self.existing_habit_4 = Habit.objects.create(
            user=self.user_2,
            place="Дома",
            time=timezone.now() + timedelta(days=1),
            action="Делать 10 раз пресс",
            is_pleasant_habit=False,
            periodicity=1,
            reward="Съесть шоколадку",
            time_to_do=60,
            is_public=False,
        )

        self.existing_habit_5 = Habit.objects.create(
            user=self.user,
            place="Дома",
            time=timezone.now() + timedelta(days=1),
            action="Делать 50 раз пресс",
            is_pleasant_habit=False,
            periodicity=1,
            reward="Съесть конфету",
            time_to_do=60,
            is_public=True,
        )

        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """Тестирование создания привычки"""
        data = {
            "user": self.user,
            "place": "В кровати",
            "time": timezone.now() + timedelta(days=1),
            "action": "Делать вакуум 5 раз",
            "is_pleasant_habit": False,
            "periodicity": 1,
            "reward": "Выпить кофе",
            "time_to_do": 120,
            "is_public": True,
        }

        response = self.client.post("/habits/habit/create/", data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habits_list(self):
        """Тестирование просмотра списка привычек"""

        response = self.client.get("/habits/own_habit/list/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_details(self):
        """Тестирование просмотра приватной привычки другого пользователя"""

        response = self.client.get(f"/habits/habit/{self.existing_habit_4.id}/details/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_public_habit_details(self):
        """Тестирование просмотра публичной привычки"""

        response = self.client.get(f"/habits/habit/{self.existing_habit_5.id}/details/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_habit(self):
        """Тестирование обновления привычки"""
        data = {
            "periodicity": 2,
        }

        response = self.client.patch(
            f"/habits/habit/{self.existing_habit_1.id}/update/", data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habit(self):
        """Тестирование удаления привычки"""

        response = self.client.delete(
            f"/habits/habit/{self.existing_habit_1.id}/delete/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
