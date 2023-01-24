from rest_framework import serializers
from habit_tracker.models import Habit

class HabitSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field="username", read_only=True)
    class Meta:
        model = Habit
        fields = ("id", "title", "goal", "unit", "owner")
