from django.urls import path
from .views import StudentListCreateView

urlpatterns = [
    # The empty string '' means the base URL for this app
    path('', StudentListCreateView.as_view(), name='student-list'),
]