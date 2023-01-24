"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from habit_tracker import views
from api import urls as api_urls
from config import settings

urlpatterns = [
    path("", views.list_habits, name="habit_list"),
    path("habits/", views.list_habits, name="habit_list"),
    path("habits/new", views.habit_new, name="habit_new"),
    path("habits/<int:habit_pk>", views.habit_detail, name="habit_detail"),
    path(
        "habits/<int:habit_pk>/results",
        views.habit_tracker,
        name="habit_tracker",
    ),
    path(
        "results/<int:tracker_pk>",
        views.habit_tracker,
        name="habit_tracker_update",
    ),
    path("admin/", admin.site.urls),
    path("accounts/", include("registration.backends.simple.urls")),
    path("api/", include(api_urls)),
]

if settings.DEBUG:
    urlpatterns += ((path("__debug__/", include("debug_toolbar.urls"))),)
