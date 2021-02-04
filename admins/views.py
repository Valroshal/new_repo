from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from admins.models import Admins, Teachers, Students, School
from admins.serializers import StudentsSerializer, TeachersSerializer, AdminsSerializer, SchoolSerializer


@api_view(['Get'])
#@permission_classes((IsAuthenticated)) - for token authentication
def students_detail_view(request):
    try:
        students = Students.objects.get()
    except ObjectDoesNotExist:
        print("doesn't exist")
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentsSerializer(students)
        return Response(serializer.data)

@api_view(['Get'])
#@permission_classes((IsAuthenticated)) - for token authentication
def teachers_detail_view(request):
    try:
        teachers = Teachers.objects.get()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TeachersSerializer(teachers)
        return Response(serializer.data)


@api_view(['Get'])
#@permission_classes((IsAuthenticated)) - for token authentication
def admins_detail_view(request):
    try:
        admins = Admins.objects.get()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AdminsSerializer(admins)
        return Response(serializer.data)

@api_view(['Get'])
#@permission_classes((IsAuthenticated)) - for token authentication
def school_detail_view(request):
    try:
        school = School.objects.get()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SchoolSerializer(school)
        return Response(serializer.data)




@api_view(['Put'])
def update_students_view(request):
    try:
        students = Students.objects.get()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

############################### permissions
    user = request.user
    if user.role == "Student":
        return Response({'response': 'no permissions'})
    else:
        if user.role == "Admin":
            if user.school != students.school:
                return Response({'response': 'no permissions'})
        else:
            if user.role == "Teacher" and user.email != students.teacher.email:
                return Response({'response': 'no permissions'})

############################################## end here permissions 
    if request.method == "PUT":

            serializer = StudentsSerializer(students, data=request.data)
            data={}
            if serializer.is_valid():
                serializer.save()
                data["success"] = "update success"
                return Response(data=data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['Put'])
def update_teachers_view(request):
    try:
        teachers = Teachers.objects.get()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

############################### permissions
    user = request.user
    if user.role == "Student" or user.role == "Teacher":
        return Response({'response': 'no permissions'})
    else:
        if user.role == "Admin":
            if user.school != teachers.school:
                return Response({'response': 'no permissions'})

############################################## end here permissions 
    if request.method == "PUT":

            serializer = TeachersSerializer(teachers, data=request.data)
            data={}
            if serializer.is_valid():
                serializer.save()
                data["success"] = "update success"
                return Response(data=data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Put'])
def update_admins_view(request):
    try:
        admins = Admins.objects.get()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

############################### permissions
    user = request.user
    if user.role == "Student" or user.role == "Teacher":
        return Response({'response': 'no permissions'})
    else:
        if user.role == "Admin":
            if user.id != admins.id:# id is automatic in django
                return Response({'response': 'no permissions'})

############################################## end here permissions 
    if request.method == "PUT":

            serializer = AdminsSerializer(admins, data=request.data)
            data={}
            if serializer.is_valid():
                serializer.save()
                data["success"] = "update success"
                return Response(data=data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







@api_view(['Delete'])
def delete_students_view(request):
    try:
        students = Students.objects.get()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

############################### permissions
    user = request.user
    if user.role == "Student":
        return Response({'response': 'no permissions'})
    else:
        if user.role == "Admin":
            if user.school != students.school:
                return Response({'response': 'no permissions'})
        else:
            if user.role == "Teacher" and user.email != students.teacher.email:
                return Response({'response': 'no permissions'})

############################################## end here permissions 
    if request.method == "DELETE":
        operation= students.delete()
        data={}
        if operation:
            data["success"] = "delete success"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)

@api_view(['Delete'])
def delete_teachers_view(request):
    try:
        teachers = Teachers.objects.get()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

############################### permissions
    user = request.user
    if user.role == "Student" or user.role == "Teacher":
        return Response({'response': 'no permissions'})
    else:
        if user.role == "Admin":
            if user.school != teachers.school:
                return Response({'response': 'no permissions'})
############################################## end here permissions 
    if request.method == "DELETE":
        operation= teachers.delete()
        data={}
        if operation:
            data["success"] = "delete success"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)



@api_view(['Delete'])
def delete_admins_view(request):
    try:
        admins = Admins.objects.get()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

############################### permissions
    user = request.user
    if user.role == "Student" or user.role == "Teacher":
        return Response({'response': 'no permissions'})
    else:
        if user.role == "Admin":
            if user.id != admins.id: # id is automatic in django
                return Response({'response': 'no permissions'})
############################################## end here permissions 
    if request.method == "DELETE":
        operation= admins.delete()
        data={}
        if operation:
            data["success"] = "delete success"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)








@api_view(['Post'])
def create_students_view(request):
    user = request.user
    students = Students.objects.create(user)
    ############################### permissions
    
    if user.role == "Student":
        return Response({'response': 'no permissions'})
    else:
        if user.role == "Admin":
            if user.school != students.school:
                return Response({'response': 'no permissions'})
        else:
            if user.role == "Teacher" and user.email != students.teacher.email:
                return Response({'response': 'no permissions'})

############################################## end here permissions
    if request.method == "POST":
        serializer = StudentsSerializer(students, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['Post'])
def create_teachers_view(request):
    user = request.user
    teachers = Teachers.objects.create(user)
    ############################### permissions
    user = request.user
    if user.role == "Student" or user.role == "Teacher":
        return Response({'response': 'no permissions'})
    else:
        if user.role == "Admin":
            if user.school != teachers.school:
                return Response({'response': 'no permissions'})
############################################## end here permissions 

    if request.method == "POST":
        serializer = TeachersSerializer(teachers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['Post'])
def create_admins_view(request):
    user = request.user
    admins = Admins.objects.create(user)
    ############################### permissions
    user = request.user
    if user.role == "Student" or user.role == "Teacher":
        return Response({'response': 'no permissions'})
    else:
        if user.role == "Admin":
            if user.id != admins.id: # id is automatic in django
                return Response({'response': 'no permissions'})
############################################## end here permissions 

    if request.method == "POST":
        serializer = AdminsSerializer(admins, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











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

       