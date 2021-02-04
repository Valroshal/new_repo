from rest_framework import serializers
from admins.models import Students, Teachers, Admins, School

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['role', 'first_name', 'last_name', 'student_since', 'email', 'birthday', 'school', 'teacher']


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ['role', 'first_name', 'last_name', 'teacher_since', 'email', 'birthday', 'school']

class AdminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = ['role', 'first_name', 'last_name', 'teacher_since', 'email', 'birthday', 'school']

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['name_school', 'address', 'phone_number']