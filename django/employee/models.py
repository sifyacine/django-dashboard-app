# employee/models.py

from django.db import models

class EmployeeBase(models.Model):
    ROLE_CHOICES = [
        ('enseignant', 'Enseignant'),
        ('secretaire', 'Secretaire'),
        ('tresorier', 'Tresorier')
    ]

    name = models.CharField(max_length=100)
    cin = models.CharField(max_length=100, unique=True)
    file = models.FileField(upload_to='uploads/')
    phone_number = models.CharField(max_length=15)
    date_of_adhesion = models.DateField()
    address = models.TextField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True

class Teacher(EmployeeBase):
    subject_taught = models.CharField(max_length=100)

class Employee(EmployeeBase):
    pass
