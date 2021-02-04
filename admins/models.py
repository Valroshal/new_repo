from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings 
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class User_Roles(AbstractUser):
    roles = ((1, "Admin"),(2, "Teacher"),(3, "Student"))
    user_roles = models.CharField(max_length=50, default=1, choices=roles)
    
    def __str__(self):
        full_name = self.first_name + " " + self.last_name #django build firatname and lastname
        return full_name


class School(models.Model):
    name_school = models.CharField(max_length=50)
    address = models.CharField(max_length=20)
    #phone_number = PhoneField(blank=True, help_text='Contact phone number', unique=True) #can be added intead
    phone_number = models.CharField(max_length=20)
    objects = models.Manager()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name_school #return school name


class Admins(models.Model):   
    role = models.OneToOneField(User_Roles, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    teaching_since = models.DateTimeField()
    instrument = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    objects = models.Manager()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Teachers(models.Model):
    role = models.OneToOneField(User_Roles, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    teaching_since = models.DateTimeField()
    instrument = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    school = models.ForeignKey(School, null=True , on_delete=models.CASCADE)
    objects = models.Manager()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        if self.first_name and self.last_name:
            full_name = self.first_name + " " + self.last_name
        return full_name #relation with user_role


class Students(models.Model):
    role = models.OneToOneField(User_Roles, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_since = models.DateTimeField()
    email = models.EmailField(max_length=254, unique=True)
    birthday = models.DateTimeField()
    school = models.ForeignKey(School, null=True ,on_delete=models.CASCADE)    #one to many
    teacher = models.ForeignKey(Teachers, null=True ,on_delete=models.CASCADE) #one to many
    objects = models.Manager()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        if self.first_name and self.last_name:
            full_name = self.first_name + " " + self.last_name
        return full_name #relation with user_role

@receiver(post_save, sender=User_Roles)
def create_user_profile(sender, instance, **kwargs):

        #Token.objects.create(user=instance) #- can be token authentication instead
        if instance.user_type==1:
            Admins.objects.create(admin=instance)
        if instance.user_type==2:
            Teachers.objects.create(admin=instance)
        if instance.user_type==3:
            Students.objects.create(admin=instance)

@receiver(post_save, sender=User_Roles)
def save_user_profile(sender, instance, **kwargs):

        if instance.user_type==1:
            instance.admins.save()
        if instance.user_type==2:
            instance.teachers.save()
        if instance.user_type==3:
            instance.students.save()

