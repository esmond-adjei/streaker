from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from streak.models import Task, Streak
from streak.api.serializers import TaskSerializer, StreakSerializer


def get_object(model, id):
    try:
        return model.objects.get(id=id)
    except model.DoesNotExist:
        raise Http404


class TaskList(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    def get(self, request, id):
        task = get_object(Task, id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, id):
        task = get_object(Task, id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        task = get_object(Task, id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreakList(APIView):
    def get(self, request):
        streaks = Streak.objects.all()
        serializer = StreakSerializer(streaks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreakSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreakDetail(APIView):
    def get(self, request, id):
        streak = get_object(Streak, id)
        serializer = StreakSerializer(streak)
        return Response(serializer.data)

    def put(self, request, id):
        streak = get_object(Streak, id)
        serializer = StreakSerializer(streak, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        streak = get_object(Streak, id)
        streak.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
