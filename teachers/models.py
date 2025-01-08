from django.db import models
from authentication.models import CustomUser
from classes.models import Class

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher_profile')
    qualifications = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='teachers/photos/', null=True, blank=True)
    subjects = models.ManyToManyField('Subject', related_name='teachers')
    assigned_classes = models.ManyToManyField(Class, related_name='teachers', blank=True)

    def __str__(self):
        return self.user.full_name
