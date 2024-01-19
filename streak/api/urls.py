# urls.py
from django.urls import path
from streak.api.views import TaskList, TaskDetail, StreakList, StreakDetail

urlpatterns = [
    path('', TaskList.as_view(), name='task-list'),
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<uuid:id>/', TaskDetail.as_view(), name='task-detail'),
    path('streaks/', StreakList.as_view(), name='streak-list'),
    path('streaks/<uuid:id>/', StreakDetail.as_view(), name='streak-detail'),
]
