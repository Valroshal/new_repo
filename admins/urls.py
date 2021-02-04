from django.urls import path

from admins.views import (
    students_detail_view,
    update_students_view,
    delete_students_view,
    create_students_view,
    teachers_detail_view,
    admins_detail_view,
    school_detail_view
)
app_name = 'tonara_ex'

urlpatterns = [
    #path('<slug>/', students_detail_view, name="student_detail"), # / only with get request
    path('students/', students_detail_view, name="student_detail"), # / only with get request
    path('students/update', update_students_view, name="update_students"),
    #path('<slug>/update', update_students_view, name="update_students"),
    path('students/delete', delete_students_view, name="delete_students"),
    #path('<slug>/delete', delete_students_view, name="delete_students"),
    path('students/create', create_students_view, name="create_students"),
    path('teachers/', teachers_detail_view, name="teachers_detail"),
    path('admins/', admins_detail_view, name="admins_detail"),
    path('school/', school_detail_view, name="school_detail"),
    
]