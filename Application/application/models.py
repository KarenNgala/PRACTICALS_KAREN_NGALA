from django.db import models
from django.contrib.auth.models import User



class Stream(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"