from .models import Habit, Tracker
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


class DatePickerInput(forms.DateInput):
    input_type = "date"


class TrackerForm(forms.ModelForm):
    habit_pk = forms.IntegerField(widget=forms.HiddenInput(), required=False, label="")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["amount"].widget.attrs.update({"class": "input"})
        self.fields["date"].widget.attrs.update({"class": "input"})

    class Meta:
        model = Tracker
        fields = ("date", "amount", "habit_pk")
        widgets = {"date": DatePickerInput()}
