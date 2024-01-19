from uuid import uuid4
from django.db import models
from django.utils import timezone


class EnumDays(models.Model):
    DAYS_CHOICES = [
        ('mon','Monday'),
        ('tue','Tuesday'),
        ('wed','Wednesday'),
        ('thu','Thursday'),
        ('fri','Friday'),
        ('sat','Saturday'),
        ('sun','Sunday'),
    ]
    day = models.CharField(max_length=3, choices=DAYS_CHOICES)
    
    class Meta:
        verbose_name_plural = 'EnumDays'

    def __str__(self):
        return str(self.day)


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # streak info 
    name = models.CharField(max_length=255, help_text='specific action, \
                                        eg: read 30 pages (specific), prepare for school (vague)')
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    # streak info - time measurement
    _completion_period = models.PositiveIntegerField(null=True, blank=True, help_text='number of days to perform tasks')
    duration_per_day = models.PositiveIntegerField(default=30, help_text='in minutes')
    start_date = models.DateField(default=timezone.now)
    start_time = models.TimeField(default=timezone.now)
    active_days = models.ManyToManyField(EnumDays)
    # audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def completion_period(self):
        return self._completion_period if self._completion_period else '-inf'
    
    def display_completion_period(self):
        return str(self._completion_period) + ' days' if self._completion_period else 'forever'
    
    def is_due(self):
        return self.active_days.filter(day=timezone.now().strftime('%a').lower()).exists()\
            and self.start_date < timezone.now().date()

    def create_streak(self):
        """checks if task is due and ensures one streak per day before creating a streak"""
        if self.is_due():
            if not self.streaks.filter(created_at__date=timezone.now().date()).exists(): # daily streak
                return Streak.objects.create(task=self, is_marked=False)

    def __str__(self):
        return f"{self.name} - {self.completion_period}"
    
    class Meta:
        ordering = ['-updated_at']


class StreakManager(models.Manager):
    def get_max_day_count_for_task(self, task):
        """
        Returns the maximum day count value for a streak.
        Raises error if the day count is greater exceeding the task completion period.
        """
        max_day_count = self.filter(task=task).aggregate(models.Max('day_count'))['day_count__max']
        if max_day_count >= task._completion_period:
            raise ValueError("Streak day_count exceeds task completion period.")
        return max_day_count if max_day_count is not None else 0

    def create(self, *args, **kwargs):
        task = kwargs.get('task')
        if task:
            max_day_count = self.get_max_day_count_for_task(task)
            kwargs['day_count'] = max_day_count + 1
        return super().create(*args, **kwargs)


class Streak(models.Model):
    objects = StreakManager()
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # streak info
    day_count = models.PositiveIntegerField(default=1, editable=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='streaks')
    is_marked = models.BooleanField(default=False)
    # audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        max_day_count = Streak.objects.get_max_day_count_for_task(self.task)
        self.day_count = max_day_count + 1       
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.task.name} {self.day_count}/{self.task.completion_period}"
    
    class Meta:
        ordering = ['task', '-created_at']