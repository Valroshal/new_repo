from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, AbstractUser


class User_Roles(AbstractUser):
    roles = ((1, "Admin"),(2, "Teacher"),(3, "Student"))
    user_roles = models.CharField(max_length=50, default=1, choices=roles)
    
    def __str__(self):
        full_name = self.first_name + " " + self.last_name #django build firatname and lastname
        return full_name


#need to run pip install django-phone-field, or can be charfield
class School(models.Model):
    name_school = models.CharField(max_length=50)
    address = models.CharField(max_length=20)
    phone_number = PhoneField(blank=True, help_text='Contact phone number', unique=True)
    objects = models.Manager()
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    def __str__(self):
        return self.name_school #return school name


class Admins(models.Model):
    #don't need first and last name - will be from teachers    
    role = models.OneToOneField(User_Roles, on_delete=models.CASCADE)
    objects = models.Manager()
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)

    def __str__(self):
        return self.first_name


class Teachers(models.Model):
    role = models.OneToOneField(User_Roles, on_delete=models.CASCADE)
    objects = models.Manager()
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)

    def __str__(self):
        if self.role.first_name and self.role.last_name:
            full_name = self.role.first_name + " " + self.role.last_name
        return full_name #relation with user_role

class TeacherProfile(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    teaching_since = models.DateTimeField()
    instrument = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    objects = models.Manager()
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)

    def __str__(self):
        return self.teacher.email


class Students(models.Model):
    role = models.OneToOneField(User_Roles, on_delete=models.CASCADE)
    objects = models.Manager()
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)

    def __str__(self):
        if self.role.first_name and self.role.last_name:
            full_name = self.role.first_name + " " + self.role.last_name
        return full_name #relation with user_role

class StudentProfile(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    student_since = models.DateTimeField()
    email = models.EmailField(max_length=254, unique=True)
    birthday = models.DateTimeField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)    #?????????????????????????????????????????
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE) #?????????????????????????????????????????????
    objects = models.Manager()
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)

    def __str__(self):
        return self.student.email


@receiver(post_save, sender=User_Roles)
def create_user_profile(sender, instance, **kwargs):
    if created:
        if instance.user_type==1:
            Admins.objects.create(admin=instance)
        if instance.user_type==2:
            Teachers.objects.create(admin=instance)
        if instance.user_type==3:
            Students.objects.create(admin=instance)

@receiver(post_save, sender=User_Roles)
def save_user_profile(sender, instance, **kwargs):
    if created:
        if instance.user_type==1:
            instance.admins.save()
        if instance.user_type==2:
            instance.teachers.save()
        if instance.user_type==3:
            instance.students.save()