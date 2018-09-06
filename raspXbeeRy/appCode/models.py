from django.db import models

class Nodo(models.Model):
    Nombre=models.CharField(max_length=50)
    Gps=models.CharField(max_length=50)
    Mac=models.CharField(max_length=50)
    Asscii_ID=models.CharField(max_length=50)
    Voltaje=models.CharField(max_length=50)
    Temperatura=models.CharField(max_length=50)
    Dir_16Bits=models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

class Protocolo_Wifi(models.Model):
    Nombre=models.CharField(max_length=150)

    def __str__(self):
        return self.Nombre

class Protocolo_Ethernet(models.Model):
    Nombre=models.CharField(max_length=150)

    def __str__(self):
        return self.Nombre

class Protocolo_Gprs(models.Model):
    Nombre=models.CharField(max_length=150)

    def __str__(self):
        return self.Nombre

class GateWay(models.Model):
    Nombre=models.CharField(max_length=150)
    Gps=models.CharField(max_length=150)
    Estado=models.CharField(max_length=150)
    localAddress=models.CharField(max_length=150)
    ForeingAddress=models.CharField(max_length=150)

    fk_ProtocoloWifi= models.OneToOneField(Protocolo_Wifi, null=True, blank=True, on_delete=models.CASCADE)
    fk_ProtocoloEthernet= models.OneToOneField(Protocolo_Ethernet, null=True, blank=True, on_delete=models.CASCADE)
    fk_ProtocoloGprs= models.OneToOneField(Protocolo_Gprs, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre

class Rel_Nodo_Gate(models.Model):
    Nombre=models.CharField(max_length=50)
    Gps=models.CharField(max_length=150)
    Mac=models.CharField(max_length=150)
    Dir_16Bits=models.CharField(max_length=150)

    fk_Nodo= models.OneToOneField(Nodo, null=True, blank=True, on_delete=models.CASCADE)
    fk_GateWay= models.OneToOneField(GateWay, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre


class Local_Data(models.Model):
    Sync=models.CharField(max_length=50)
    Fecha=models.CharField(max_length=150)
    Mac=models.CharField(max_length=150)
    Dir_16Bits=models.CharField(max_length=150)

    fk_Nodo= models.OneToOneField(Nodo, null=True, blank=True, on_delete=models.CASCADE)
    fk_GateWay= models.OneToOneField(GateWay, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre
