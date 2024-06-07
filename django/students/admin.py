from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'cin', 'emission_date', 'birth_date', 'birth_place', 'phone_number', 'address', 'student_class', 'file')
    search_fields = ('name', 'cin', 'birth_place', 'student_class')
    list_filter = ('emission_date', 'birth_date', 'student_class')
