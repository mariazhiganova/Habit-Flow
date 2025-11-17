from django.utils import timezone
from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    pleasant_habit = serializers.PrimaryKeyRelatedField(
        queryset=Habit.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = Habit
        fields = (
            "id",
            "place",
            "time",
            "action",
            "is_pleasant_habit",
            "pleasant_habit",
            "periodicity",
            "reward",
            "time_to_do",
            "is_public",
        )

        extra_kwargs = {"user": {"read_only": True}}

    def validate(self, attrs):
        pleasant_habit = attrs.get("pleasant_habit")
        reward = attrs.get("reward")
        is_pleasant_habit = attrs.get("is_pleasant_habit")
        time_to_do = attrs.get("time_to_do")
        periodicity = attrs.get("periodicity")
        time = attrs.get("time")

        if time:
            attrs["time"] = time.replace(second=0, microsecond=0)

            if time < timezone.now():
                raise serializers.ValidationError(
                    {"time": "Время выполнения должно быть в будущем"}
                )

        if pleasant_habit and reward:
            raise serializers.ValidationError(
                "Не может быть заполнено и поле вознаграждения, и поле связанной привычки"
            )
        if pleasant_habit:
            if not pleasant_habit.is_pleasant_habit:
                raise serializers.ValidationError(
                    "Связанная привычка должна быть приятной"
                )

        if is_pleasant_habit:
            if reward:
                raise serializers.ValidationError(
                    "У приятной привычки не может быть вознаграждения"
                )

            if pleasant_habit:
                raise serializers.ValidationError(
                    "Приятная привычка не может иметь связанную привычку"
                )

        if time_to_do and time_to_do > 120:
            raise serializers.ValidationError(
                "Время выполнения должно быть не более 120 секунд"
            )

        if periodicity:
            if periodicity > 7:
                raise serializers.ValidationError(
                    "Нельзя выполнять привычку реже, чем 1 раз в 7 дней"
                )
            if periodicity == 0:
                raise serializers.ValidationError(
                    "Нельзя никогда не повторять выполнение привычки"
                )

        return attrs
