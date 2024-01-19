from django.contrib import admin

from .models import Task, Streak, EnumDays


admin.site.register(Task)
admin.site.register(Streak)
admin.site.register(EnumDays)
