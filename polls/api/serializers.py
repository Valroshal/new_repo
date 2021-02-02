from rest_framework import serializers

from poll.models import Student, Teacher, School

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_since', 'email', 'birthday']
