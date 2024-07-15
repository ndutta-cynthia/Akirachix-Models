from django.urls import path
from .views import StudentListView
from .views import ClassroomListView
from .views import TeacherListView
from .views import CourseListView

urlpatterns= [
    path("students/" , StudentListView.as_view(),name='student_list_view'),
]
urlpatterns= [
    path("teachers/" , TeacherListView.as_view(),name='teacher_list_view'),
]

urlpatterns= [
    path("course/" , CourseListView.as_view(),name='course_list_view'),
]


urlpatterns= [
    path("classroom/" , ClassroomListView.as_view(),name='classroom_list_view'),
]