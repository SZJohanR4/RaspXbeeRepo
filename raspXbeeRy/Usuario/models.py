from django.db import models
from django.contrib.auth.models import User
from appCode.models import SimCard, Ethernet, Wifi

class Usuario(models.Model):
    Nombre=models.OneToOneField(User, on_delete=models.CASCADE)
    Password=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)

    def __str__(self):
        return self.Nombre


class Log(models.Model):
    Accion=models.CharField(max_length=50)
    Fecha=models.CharField(max_length=50)
    Donde=models.CharField(max_length=50)

    FK_idUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return self.Date


class Conexion(models.Model):
    Fecha=models.CharField(max_length=50)

    FK_idUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    FK_idSimCard=models.ForeignKey(SimCard, on_delete=models.CASCADE)
    FK_idEthernet=models.ForeignKey(Ethernet, on_delete=models.CASCADE)
    FK_idWifi=models.ForeignKey(Wifi, on_delete=models.CASCADE)
