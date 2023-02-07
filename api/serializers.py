from rest_framework import serializers
from habit_tracker.models import Habit, Tracker, User

class HabitSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field="username", read_only=True)
    class Meta:
        model = Habit
        fields = ("id", "title", "goal", "unit", "owner")


class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = ('amount', 'date')

class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("avatar",)

    def update(self, instance, validated_data):
        file = self.initial_data.get("file")
        if file is not None:
            instance.avatar.save(file.name, file)
        return instance
