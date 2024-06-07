from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    cin = models.CharField(max_length=20)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    emission_date = models.DateField()
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    student_class = models.CharField(max_length=50)

    def __str__(self):
        return self.name
