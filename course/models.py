from django.db import models
from django.db.models.manager import BaseManager

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    credits = models.PositiveIntegerField()
    department = models.CharField(max_length=50)
    instructor = models.CharField(max_length=100)
    is_elective = models.BooleanField(default=False)
    prerequisites = models.TextField()
    max_capacity = models.PositiveIntegerField()
    duration_weeks = models.PositiveIntegerField()

    objects:BaseManager['Course']


    def __str__(self):
        return f"{self.course_name} {self.course_code}"