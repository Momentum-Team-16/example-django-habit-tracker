from django.urls import path, include
from . import views

urlpatterns = [
  path("habits/", views.HabitListAPIView.as_view(), name="list_habits"),
  path('api-auth/', include('rest_framework.urls')),
]
