from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, Tracker
from .forms import HabitForm, TrackerForm
from django.contrib.auth.decorators import login_required
import datetime

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

@login_required
def habit_tracker(request, habit_pk=None, tracker_pk=None):
    habit_pk_for_lookup = habit_pk or request.POST.get("habit_pk")
    habit = get_object_or_404(Habit, pk=habit_pk_for_lookup)
    view_context = {"habit": habit}
    if request.method == "GET":
        record_date = datetime.date.today()
        tracker, _ = habit.trackers.get_or_create(date=record_date)
    else:
        tracker_instance = Tracker.objects.get(pk=tracker_pk)
        form = TrackerForm(data=request.POST, instance=tracker_instance)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.habit = habit
            tracker.save()

    if tracker:
        date_value_for_form = tracker.date
    else:
        date_value_for_form = datetime.date.today()
    view_context.update(
        form=TrackerForm(
            initial={"date": date_value_for_form, "habit_pk": habit.pk}
        ),
        tracker=tracker,
        habit=habit,
    )

    return render(request, "habit_tracker/habit_results.html", view_context)
