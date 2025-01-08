from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('parent', 'Parent'),
        ('student', 'Student'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    @property
    def full_name(self):
        # Combine first_name and last_name dynamically
        return f"{self.first_name} {self.last_name}".strip()