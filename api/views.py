from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from habit_tracker.models import Habit
from . import serializers

# Create your views here.
# class HabitListView(APIView):
#     def get(self, request, format=None):
#         """
#         Return a list of all habits.
#         """
#         habits = Habit.objects.all()
#         serializer = serializers.HabitSerializer(habits, many=True)
#         # I need to serialize this data
#         return Response(serializer.data)


#     def post(self, request, format=None):
#         """
#         Create a new habit for the logged in user
#         """
#         # get the user
#         serializer = serializers.HabitSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(owner = request.user)
#         # create a new habit for that user using the serializer
#         # return the newly created habit
#         return Response(serializer.data)


class HabitListAPIView(generics.ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = serializers.HabitSerializer


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
