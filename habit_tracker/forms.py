from .models import Habit
from django import forms

class HabitForm(forms.ModelForm):
    # https://docs.djangoproject.com/en/4.0/ref/forms/widgets/#styling-widget-instances-1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "input"})
        self.fields["goal"].widget.attrs.update({"class": "input"})

    class Meta:
        model = Habit
        fields = ("title", "goal")
        labels = {
            "title": "What habit do you want to build?",
            "goal": "What is your target number for daily reps of this habit?",
        }
