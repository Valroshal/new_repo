from django.urls import path

from admins.views import (
    students_detail_view,
    update_students_view,
    delete_students_view,
    create_students_view,
    teachers_detail_view,
    update_teachers_view,
    delete_teachers_view,
    create_teachers_view,
    admins_detail_view,
    update_admins_view,
    delete_admins_view,
    create_admins_view,
    school_detail_view
)
app_name = 'tonara_ex'

urlpatterns = [
    path('students/', students_detail_view, name="student_detail"), # / only with get request
    path('students/update', update_students_view, name="update_students"),
    path('students/delete', delete_students_view, name="delete_students"),
    path('students/create', create_students_view, name="create_students"),
    path('teachers/', teachers_detail_view, name="teachers_detail"),
    path('teachers/update', update_teachers_view, name="update_teachers"),
    path('teachers/delete', delete_teachers_view, name="delete_teachers"),
    path('teachers/create', create_teachers_view, name="create_teachers"),
    path('admins/', admins_detail_view, name="admins_detail"),
    path('admins/update', update_admins_view, name="update_admins"),
    path('admins/delete', delete_admins_view, name="delete_admins"),
    path('admins/create', create_admins_view, name="create_admins"),
    path('school/', school_detail_view, name="school_detail"),
    
]