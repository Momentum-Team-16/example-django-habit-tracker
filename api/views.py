from django.shortcuts import  get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics, status, permissions, parsers
from rest_framework.response import Response
from habit_tracker.models import Habit, User
from . import serializers

from django.db import IntegrityError

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
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TrackerListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.TrackerSerializer

    def get_queryset(self):
        habit = get_object_or_404(Habit, pk=self.kwargs["habit_pk"])
        return habit.trackers.all()

    def perform_create(self, serializer):
        # TODO: handle the Integrity Error if a tracker for this date exists already
        habit = get_object_or_404(Habit, pk=self.kwargs["habit_pk"])
        serializer.save(habit=habit)

    def create(self, request, *args, **kwargs):
        try:
            super().create(request, *args, **kwargs)
        except IntegrityError as error:
            return Response(error.message, status=status.HTTP_400_BAD_REQUEST)

class UserAvatarCreateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserAvatarSerializer
    parser_classes = [parsers.FileUploadParser]

    def get_object(self):
        return self.request.user

