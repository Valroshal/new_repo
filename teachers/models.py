# from django.db import models
# from django.contrib.auth.models import User, AbstractUser, BaseUserManager
# from django.urls import reverse


# # class MyAccountManager(BaseUserManager):
# #     def create_user()

# class Teacher(AbstractUser):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     teaching_since = models.DateTimeField()
#     instrument = models.CharField(max_length=20)
#     email = models.EmailField(max_length=254, unique=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE) # reference key - connection from school to teacher, only one school for teacher
#     school = ?
#     #role = administrator/regular teacher #- is to be here or not?
#     is_admin = models.BooleanField(default=False)

#     REQUIRED_FIELDS = []
#     # not needed to be, optional
#     # class Meta:
#     #     verbose_name = 'Student'
#     #     verbose_name_plural = 'Students of teacher' 
#     def has_module_perms(self, app_label):
#         return True

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def __str__(self):
#         return self.first_name

#     def get_absolute_url(self):
#         return reverse('index', kwargs={'username': self.username})

#     ####def submittion_delete(self): # need to check how to to do it

# class Student(AbstractUser):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     student_since = models.DateTimeField()
#     email = models.EmailField(max_length=254, unique=True)
#     birthday = models.DateTimeField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE) # reference key - connection from teacher to student, teacher id, can be only one teacher

    
#     def __str__(self):
#         return self.first_name

#     def get_absolute_url(self):
#         return reverse('index', kwargs={'pk': self.pk})

# #need to run pip install django-phone-field
# class School(models.Model):
#     name_school = models.CharField(max_length=50)
#     address = models.CharField(max_length=20)
#     phone_number = PhoneField(blank=True, help_text='Contact phone number', unique=True)
#     # reference key #not here in student/teacher###### - connection from school to admin, teachers and students

#     def __str__(self):
#         return self.name_school

#     # def get_absolute_url(self):
#     #     return reverse('index', kwargs={'pk': self.pk})


# # def __str__(self):
# #   return self.first_name