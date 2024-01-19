# urls.py
from django.urls import path
from streak.api.views import TaskList, TaskDetail, StreakList, StreakDetail

urlpatterns = [
    path('', TaskList.as_view(), name='task-list'),
    path('task/', TaskList.as_view(), name='task-list'),
    path('task/<uuid:id>/', TaskDetail.as_view(), name='task-detail'),
    path('streak/', StreakList.as_view(), name='streak-list'),
    path('streak/<uuid:id>/', StreakDetail.as_view(), name='streak-detail'),
]
