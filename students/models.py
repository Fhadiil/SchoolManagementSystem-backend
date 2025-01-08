from django.db import models
from authentication.models import CustomUser
from classes.models import Class

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    age = models.PositiveIntegerField()
    contact = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='students/photos/', null=True, blank=True)
    documents = models.FileField(upload_to='students/documents/', null=True, blank=True)
    assigned_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}".strip()

    def __str__(self):
        return self.full_name

