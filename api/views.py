from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from student.models import Student
from .serializers import StudentSerializer
from  course.models import Course
from .serializers import CourseSerializer
from classroom.models import Classroom
from .serializers import ClassroomSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer
from classperiod.models import Class_Period
from .serializers import Class_PeriodSerializer
from rest_framework import status


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name= request.query_params.get("first_name")
        first_name= request.query_params.get("country")
        if first_name:
            students.filter(first_name=first_name)
        # if email:
        #     students.filter(count=country)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class  CourseListView(APIView):
    def get(self,request):
        courses= Course.objects.all()
        serializer = CourseSerializer(Course,many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ClassroomSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TeacherListView(APIView):
    def get (self,request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher,many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TeacherSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class  ClassesListView (APIView):
    def get (self,request):
        classes = Classroom.objects.all()
        serializer = ClassroomSerializer(classes,many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ClassroomSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ClassPeriodListView(APIView):
    def get (self,request):
        classperiod = Class_Period.objects.all()
        serializer = classperiod(classperiod,many=True)
        return Response(serializer.data)
    
class StudentDetailView(APIView):
    def get (self, request,id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    def put (self, request,id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        student = Student.objects.get(id = id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    # def enrol_student(self, student, course_id):
    #     Course= Course.objects.get(id=course_id)
    #     student.courses.add(Course)
    # def post(self, request,id):
    #     student= Student.objects.get(id=id)
    #     action=request.data.get("course_id")
    #     self.enrol_student(status= status.HTTP_202_ACCEPTED)
        # self.enrol_student(status= status.HTTP_202_ACCEPTED)
        

class TeacherDetailView(APIView):
    def get (self, request,id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    def put (self, request,id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        teacher = Teacher.objects.get(id = id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
class ClassDetailView(APIView):
    def get (self, request,id):
        classes= Classroom.objects.get(id = id)
        serializer = ClassroomSerializer(classes)
        return Response(serializer.data)
    def put (self, request,id):
        classes = Classroom.objects.get(id = id)
        serializer = StudentSerializer(classes,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        classes = Classroom.objects.get(id = id)
        classes.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
class CourseDetailView(APIView):
    def get (self, request,id):
        course = Course.objects.get(id = id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    def put (self, request,id):
        course = Course.objects.get(id = id)
        serializer = StudentSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        course = Student.objects.get(id = id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
class ClassPeriodDetailView(APIView):
    def get (self, request,id):
        classperiod = Class_Period.objects.get(id = id)
        serializer = Class_PeriodSerializer(classperiod)
        return Response(serializer.data)
    def put (self, request,id):
        classperiod = Class_Period.objects.get(id = id)
        serializer = ClassroomSerializer(classperiod,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        classperiod = Class_Period.objects.get(id = id)
        classperiod.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    

    def post(self, request):
        teacher_id = request.data.get("teacher_id")
        course_id = request.data.get("course_id")
        day = request.data.get("day")
        start_time = request.data.get("start_time")
        end_time = request.data.get("end_time")
        self.create_class_period(teacher_id, course_id, day, start_time, end_time)
        return Response(status=status.HTTP_202_ACCEPTED)
    def create_class_period(self, teacher_id, course_id, day, start_time, end_time):
        teacher = Teacher.objects.get(id=teacher_id)
        course = Course.objects.get(id=course_id)
        class_period = Class_Period.objects.create(teacher=teacher, course=course, day=day, start_time=start_time, end_time=end_time)
        class_period.save()
    
class WeeklyTimetableView(APIView):
    def get(self, request):
        class_periods = Class_Period.objects.all()
        serializer = Class_PeriodSerializer(class_periods, many=True)
        return Response(serializer.data)