from django.shortcuts import render

from classroom.models import Classroom
from .serializers import ClassroomSerializer
from rest_framework.views import APIView
from rest_framework.views import Response
from course.models import Course
from .serializers import CourseSerializer
from student.models import Student
from teacher.models import Teacher
from .serializers import TeacherSerializer
from .serializers import StudentSerializer

# Create your views here.

class StudentListView(APIView):
    def get(self,request):
        students= Student.objects.all()
        serializer= StudentSerializer(students,many=True)
        return Response(serializer.data)
class ClassroomListView(APIView):
    def get(self,request):
        classrooms= Classroom.objects.all()
        serializer= ClassroomSerializer(classrooms,many=True)
        return Response(serializer.data)
    
class TeacherListView(APIView):
    def get(self,request):
        teachers= Teacher.objects.all()
        serializer= TeacherSerializer(teachers,many=True)
        return Response(serializer.data)

class CourseListView(APIView):
    def get(self,request):
        courses= Course.objects.all()
        serializer= CourseSerializer(courses,many=True)
        return Response(serializer.data)
