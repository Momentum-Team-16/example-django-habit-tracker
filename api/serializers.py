from rest_framework import serializers
from habit_tracker.models import Habit, Tracker

class HabitSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field="username", read_only=True)
    class Meta:
        model = Habit
        fields = ("id", "title", "goal", "unit", "owner")


class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = ('amount', 'date')

