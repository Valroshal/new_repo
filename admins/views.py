from django.shortcuts import render, redirect
#from django.http import HttpResponse, HttpResponseRedirect
#from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
#from rest_framework.permissions import IsAuthenticated

from admins.models import Admins, Teachers, Students, School
from admins.serializers import StudentsSerializer, TeachersSerializer, AdminsSerializer, SchoolSerializer



@api_view(['Get'])
def students_detail_view(request, slug):
    try:
        students = Students.objects.get(slug=slug)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentsSerializer(students)
        return Response(serializer.data)



######## try to give permissions#####################################################################################
@api_view(['Put'])
def update_students_view(request, slug):
    try:
        students = Students.objects.get(slug=slug)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
############################### from here my code
        if (request.user.role == "Admin" and request.user.school.name_school == students.user.school.name_school) or
        (request.user.role == "Teacher" request.user.email == students.user.teacher.email)
############################################## end here permissions don't know if will work
            serializer = StudentsSerializer(students, data=request.data)
            data={}
            if serializer.is_valid():
                serializer.save()
                data["success"] = "update success"
                return Response(data=data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
############################### from here my code 
        else:
            data["failure"] = "no permissions"
            return Response(data=data)
############################################## end here permissions don't know if will work





@api_view(['Delete'])
def delete_students_view(request, slug):
    try:
        students = Students.objects.get(slug=slug)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation= students.delete()
        data={}
        if operation:
            data["success"] = "delete success"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)

@api_view(['Post'])
def create_students_view(request):
    account = request.user
    students = Students(school=account)
    
    if request.method == "POST"
        serializer = StudentsSerializer(students, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer=dataת, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







@api_view(['Get'])
def teachers_detail_view(request, slug):
    try:
        teachers = Teachers.objects.get(slug=slug)
    except Teachers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TeachersSerializer(teachers)
        return Response(serializer.data)


@api_view(['Get'])
def admins_detail_view(request, slug):
    try:
        admins = Admins.objects.get(slug=slug)
    except Admins.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AdminsSerializer(admins)
        return Response(serializer.data)

@api_view(['Get'])
def school_detail_view(request, slug):
    try:
        school = School.objects.get(slug=slug)
    except School.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SchoolSerializer(school)
        return Response(serializer.data)





# def index(request):
#     #return HttpResponse("Hello, world. You're at the polls index.")
#     #with html
#     context = {'students': 'some students',#Student.objects.all(),
#               'teachers': 'some teachers',#Teacher.objects.all(),
#               'schools': 'some schools'} #School.objects.all()  }
#     return render(request, 'polls/index.html', context)

# def doLogin(request):
#     if request.method!="POST":
#         return HttpResponse ("error") # can be html code inside
#     else:
#         user=EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
#         if user!=None:
#             return HttpResponse("Email: " + request.POST.get("email")+" Password: " +request.POST.get("password"))
#         else:
#             return HttpResponse("invalid login")

# def GetUserDetails(request): ######read
#     if request.user !=None:
#         return HttpResponse("User: " + request.user.email + " user_type: " + request.user.user_type) #user_type = role
#     else:
#         return HttpResponse("login first")

# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect("/")










# class StudentCreateView(LoginRequiredMixin, CreateView):
#     model = Student
#     fields = ['first_name', 'last_name', 'student_since', 'email', 'birthday']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

# class TeacherCreateView(LoginRequiredMixin, CreateView):
#     model = Teacher
#     fields = ['first_name', 'last_name', 'teaching_since', 'instrument', 'email', 'school', 'role']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

# class SchoolCreateView(LoginRequiredMixin, CreateView):
#     model = School
#     fields = ['name_school', 'address', 'phone_number']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


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

       