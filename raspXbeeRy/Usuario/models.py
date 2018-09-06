from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    Nombre=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)

    def __str__(self):
        return self.Nombre


 class Log(models.Model):
    Date=models.CharField(max_length=50)
    Action=models.CharField(max_length=50)

    def __str__(self):
        return self.Daate