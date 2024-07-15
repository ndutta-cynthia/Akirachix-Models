from django.db import models
from django.db.models.manager import BaseManager

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=10, unique=True)
    date_of_birth = models.DateField()
    grade = models.PositiveIntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    enrollment_date = models.DateField()
    is_active = models.BooleanField(default=True)

    objects:BaseManager['Student']
    


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
