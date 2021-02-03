from rest_framework import serializers
#from django.contrib.auth.models import User
from admins.models import Students, Teachers, Admins, School

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['first_name', 'last_name', 'student_since', 'email', 'birthday']


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ['first_name', 'last_name', 'student_since', 'email', 'birthday']

class AdminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = ['first_name', 'last_name', 'student_since', 'email', 'birthday']

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['name_school', 'address', 'phone_number']