# employee/admin.py

from django.contrib import admin
from .models import Employee, Teacher

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'cin', 'phone_number', 'role', 'monthly_salary', 'date_of_adhesion')
    search_fields = ('name', 'cin', 'phone_number', 'role')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'cin', 'phone_number', 'role', 'monthly_salary', 'date_of_adhesion', 'subject_taught')
    search_fields = ('name', 'cin', 'phone_number', 'role', 'subject_taught')
