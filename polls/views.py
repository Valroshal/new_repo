from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.generic import CreateView
from gjango.contrib.auth.mixins import LoginRequiredMixin
from .models import (
    Teacher, 
    Student, 
    School
    )


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #with html
    context = {'students': 'some students',#Student.objects.all(),
              'teachers': 'some teachers',#Teacher.objects.all(),
              'schools': 'some schools'} #School.objects.all()  }
    return render(request, 'polls/index.html', context)

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'student_since', 'email', 'birthday']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    fields = ['first_name', 'last_name', 'teaching_since', 'instrument', 'email', 'school', 'role']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SchoolCreateView(LoginRequiredMixin, CreateView):
    model = School
    fields = ['name_school', 'address', 'phone_number']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


 ##########or###############
# class.MyLoginView(LoginView):
#     #template_name = 'login.html'
#     form_class = AuthUserForm
#     success_url = reverse_lazy(edit_page)

# class MyObtainTokenPairView(TokenObtainPairView):
#     permission_classes = (AllowAny,)
#     serializer_class = MyTokenObtainPairSerializer

# def create(request):
#     if request.method == 'POST':
#         print ('**')
#         print (request.POST)
#         print ('**')
#     else:
#         return redirect('/')

       