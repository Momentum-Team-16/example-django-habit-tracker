from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.username


# https://docs.djangoproject.com/en/4.1/topics/db/models/#abstract-base-classes
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
      abstract = True


class Habit(BaseModel):
    title = models.CharField(max_length=255)
    goal = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habits")

    def __str__(self):
        return self.title



class Tracker(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="trackers")
    amount = models.PositiveIntegerField(default=0)
    date = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["date", "habit"], name="unique_for_habit_and_date"
            )
        ]

    def __str__(self):
        return f"Tracker for {self.habit.title} on {self.date}"

    def __repr__(self):
        return f"<Record for {self.habit.title} pk={self.pk}>"
