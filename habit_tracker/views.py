from django.shortcuts import render
from .models import Habit
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list_habits(request):
    # make a query for all the habits
    habits = Habit.objects.all()
    # need a view context -- that's the data the template will use
    context = {"habits": habits, "greeting": "Hi hello"}
    # have a template to return
    return render(request, "habit_tracker/habit_list.html", context)
