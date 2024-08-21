from django.urls import path
from .views import ClassPeriodListView
# from .views import CourseListViews
from .views import CourseListView
# from .views import ClassroomListViews
# from .views import ClassPeriodSerializer
from .views import ClassroomSerializer
from .views import StudentDetailView
# from .views import StudentListViews
from .views import StudentListView
# from .views import TeacherListViews
from .views import TeacherListView
from .views import TeacherDetailView
from .views import CourseDetailView
# from .views import Class_PeriodDetailView
# from .views import ClassroomDetailView
from .views import ClassPeriodDetailView
from .views import ClassesListView
from .views import ClassDetailView
# from .views import WeeklyTimetableView
from .views import WeeklyTimetableView

urlpatterns = [
    path("student/",StudentListView.as_view(),name = "student_list_view"),
    path("teacher/",TeacherListView.as_view(),name = "teacher_list_view"),
    path("course/",CourseListView.as_view(),name = "course_list_view"),
    path("classroom/",ClassesListView.as_view(),name = "class_room_list_view"),
    path("class_period/",ClassPeriodListView.as_view(),name = "classperiod_list_view"),
    path("student/<int:id>/",StudentDetailView.as_view(), name= "studentdetail_view"),
    path ("teacher/<int:id>/", TeacherDetailView.as_view(), name = "teacherdetail_view"),
    path ("course/<int:id>/", CourseDetailView.as_view(), name = "coursedetail_view"),
    path ("classperiod/<int:id>/", ClassPeriodDetailView.as_view(), name = "classperiod_detail_vire"),
    path ("classroom/<int:id>/", ClassDetailView.as_view(), name = "classroomdetail_view"),
    path('timetable/', WeeklyTimetableView.as_view(), name='weekly_timetable')
]