from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitDestroyAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    OwnHabitListAPIView, PublicHabitListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path("habit/create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("own_habit/list/", OwnHabitListAPIView.as_view(), name="own_habit_list"),
    path(
        "public_habit/list/", PublicHabitListAPIView.as_view(), name="public_habit_list"
    ),
    path("habit/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path(
        "habit/<int:pk>/details/", HabitRetrieveAPIView.as_view(), name="habit_details"
    ),
    path("habit/<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habit_delete"),
]
