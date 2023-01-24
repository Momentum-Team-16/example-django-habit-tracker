from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit
from .forms import HabitForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list_habits(request):
    # make a query for all the habits
    habits = request.user.habits.all()
    # need a view context -- that's the data the template will use
    context = {"habits": habits, "form": HabitForm()}
    # have a template to return
    return render(request, "habit_tracker/habit_list.html", context)


def habit_new(request):
    if request.method == "POST":
          form = HabitForm(data=request.POST)
          if form.is_valid():
              habit = form.save(commit=False)
              habit.owner = request.user
              habit.save()
              return redirect("habit_list")

    return render(request, "habit_tracker/habit_new.html", {"form": HabitForm()})

def habit_detail(request, habit_pk):
    habit = get_object_or_404(Habit, pk=habit_pk)

    return render(request, "habit_tracker/habit_detail.html", {"habit": habit})
