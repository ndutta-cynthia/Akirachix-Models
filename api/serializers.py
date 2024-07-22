# from rest_framework import serializers
# from student.models import Student
# from course.models import Course
# from teacher.models import Teacher
# from classroom.models import Classroom


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields= "__all__"

# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields= "_all_"

# class TeacherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Teacher
#         fields= "__all__"

# class ClassroomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Classroom
#         fields= "__all__"

from classperiod.models import Class_Period
from classroom.models import Classroom
from course.models import Course
from student.models import Student
from rest_framework import serializers
from teacher.models import Teacher
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = "__all__"
class Class_PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Period
        fields = '__all__'
