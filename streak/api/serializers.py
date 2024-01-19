from rest_framework import serializers
from streak.models import Task, Streak
from streak.utils import getEndDate


class TaskSerializer(serializers.ModelSerializer):
    active_days = serializers.SerializerMethodField()
    completion_period = serializers.SerializerMethodField()
    end_date = serializers.SerializerMethodField()

    class Meta:
        model = Task
        exclude = ('_completion_period',)
        include = ('end_date',)
    
    def get_active_days(self, obj):
        return [day['day'] for day in obj.active_days.values()]
    
    def get_completion_period(self, obj):
        return obj.completion_period
    
    def get_end_date(self, obj):
        return getEndDate(obj.start_date, len(self.get_active_days(obj)), obj.completion_period)


class StreakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streak
        fields = '__all__'
