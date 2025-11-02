from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "place",
        "time",
        "action",
        "is_pleasant_habit",
        "is_public",
    )
    list_filter = ("is_pleasant_habit", "is_public", "periodicity")
    search_fields = ("action", "place")
