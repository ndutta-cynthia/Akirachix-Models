from django.db import models
from django.db.models.manager import BaseManager

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=20)
    hire_date = models.DateField()
    is_fulltime = models.BooleanField(default=True)
    office_number = models.CharField(max_length=10)
    subjects_taught = models.TextField()
    
    objects:BaseManager['Teacher']

def __str__(self):
    return f"{self.first_name} {self.last_name}"
