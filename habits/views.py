from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView

from habits.models import Habit
from habits.pagination import HabitsPagination
from habits.permissions import IsOwnerPermission
from habits.serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitRetrieveAPIView(RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerPermission]


class OwnHabitListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitsPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitsPagination

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitUpdateAPIView(UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerPermission]


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerPermission]
