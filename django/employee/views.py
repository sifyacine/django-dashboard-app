# employee/views.py

from rest_framework import viewsets
from .models import Employee, Teacher
from .serializers import EmployeeSerializer, TeacherSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
