from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Habit, Tracker

# Register your models here.
admin.site.register(Habit)
admin.site.register(Tracker)
admin.site.register(User, UserAdmin)
