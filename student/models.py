from django.db import models

# Create your models here.
from django.db import models


class Student(models.Model):
    """
    Student model to store student information
    """
    first_name = models.CharField(max_length=50)  # First name - text up to 50 chars
    last_name = models.CharField(max_length=50)  # Last name - text up to 50 chars
    email = models.EmailField(unique=True)  # Email - must be unique
    roll_number = models.CharField(max_length=20, unique=True)  # Roll number - unique

    def __str__(self):
        """This makes students show nicely in the admin panel"""
        return f"{self.first_name} {self.last_name} ({self.roll_number})"