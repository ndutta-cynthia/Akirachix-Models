from django.db import models
from django.db.models.manager import BaseManager

class Classroom(models.Model):
    class_name = models.CharField(max_length=100)
    class_code = models.CharField(max_length=30, unique=True)
    teacher_name = models.CharField(max_length=150)
    room_number = models.CharField(max_length=10)
    schedule = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    max_students = models.PositiveIntegerField()
    current_students = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    objects:BaseManager['Classroom']

    def __str__(self):
         return f"{self.class_name} {self.class_code}"
