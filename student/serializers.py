from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer for converting Student objects to/from JSON
    """
    class Meta:
        model = Student          # Which model to use
        fields = '__all__'       # Include all fields from the model