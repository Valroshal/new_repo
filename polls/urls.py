from django.urls import path
from polls.models import StudentCreateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/new', StudentCreateView.as_view(), name='student-create'),
    path('teacher/new', TeacherCreateView.as_view(), name='teacher-create'),

]
