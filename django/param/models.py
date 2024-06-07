# param/models.py
from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    target_line = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    website = models.URLField()
    address = models.TextField()
    logo = models.FileField(upload_to='logos/')

    def __str__(self):
        return self.name
