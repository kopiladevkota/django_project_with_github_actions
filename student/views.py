from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    """
    API endpoint that allows:
    - GET: List all students
    - POST: Create a new student
    """
    queryset = Student.objects.all()  # Get all students from database
    serializer_class = StudentSerializer  # Use our serializer