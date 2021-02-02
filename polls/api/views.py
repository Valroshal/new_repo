from rest_framework import ststus
from rest_framework.response import Response
from rest_framework.response import api_view

##from account.models import Account # I didn't have it in code. why I need? 
from polls.models import Student, Teacher, School
from polls.api.serializers import StudentSerializer