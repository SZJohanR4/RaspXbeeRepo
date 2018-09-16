from django.db import models

class GateWay(models.Model):
    Nombre=models.CharField(max_length=45)
    LatCoord=models.CharField(max_length=45)
    LongCoord=models.CharField(max_length=45)
    Estado=models.CharField(max_length=45)
    localAddress=models.CharField(max_length=150)
    ForeingAddress=models.CharField(max_length=150)

    def __str__(self):
        return self.Nombre


class Nodo(models.Model):
    Ip=models.CharField(max_length=45)
    Temperatura=models.CharField(max_length=45)
    Voltaje=models.CharField(max_length=45)
    Estado=models.CharField(max_length=45)
    LatCoord=models.CharField(max_length=45)
    LongCoord=models.CharField(max_length=45)
    Mac=models.CharField(max_length=45)
    Dir_16Bits=models.CharField(max_length=45)

    def __str__(self):
        return self.Ip

class Gate_Nodo(models.Model):
    FK_idGateWay=models.ForeignKey(GateWay, on_delete=models.CASCADE)
    FK_idNodo=models.ForeignKey(Nodo, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Wifi(models.Model):
    Direccion=models.CharField(max_length=150)
    MascaraRed=models.CharField(max_length=150)
    BroadCast=models.CharField(max_length=150)
    Dns_1=models.CharField(max_length=150)
    Dns_2=models.CharField(max_length=150)
    Protocolo=models.CharField(max_length=150)
    Canal=models.CharField(max_length=150)

    def __str__(self):
        return self.Nombre

class Wifi_Conex_Gate(models.Model):
    FK_idWifi=models.ForeignKey(Wifi, on_delete=models.CASCADE)
    FK_idGateWay=models.ForeignKey(GateWay, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class SimCard(models.Model):
    Nombre=models.CharField(max_length=150)
    Operador=models.CharField(max_length=45)
    CardPin=models.CharField(max_length=45)
    UserSim=models.CharField(max_length=45)
    PasswordSim=models.CharField(max_length=45)
    Estado=models.CharField(max_length=45)

    def __str__(self):
        return self.Nombre

class Sim_Conex_Gate(models.Model):
    FK_idSimCard=models.ForeignKey(SimCard, on_delete=models.CASCADE)
    FK_idGateWay=models.ForeignKey(GateWay, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Ethernet (models.Model):
    ModoConex=models.CharField(max_length=50)
    Estado=models.CharField(max_length=150)

    def __str__(self):
        return self.ModoConex

class Ether_Conex_Gate(models.Model):
    FK_idEthernet=models.ForeignKey(Ethernet, on_delete=models.CASCADE)
    FK_idGateWay=models.ForeignKey(GateWay, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
