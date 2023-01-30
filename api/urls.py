from django.urls import path, include
from . import views

urlpatterns = [
  path("habits/", views.HabitListAPIView.as_view(), name="list_habits"),
  path("habits/<int:habit_pk>/trackers", views.TrackerListCreateAPIView.as_view(), name="trackers_by_habit"),
  path('api-auth/', include('rest_framework.urls')),
  path('auth/', include('djoser.urls')),
  path('auth/', include('djoser.urls.authtoken')),
]
