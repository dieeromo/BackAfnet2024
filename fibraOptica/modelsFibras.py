from django.db import models
from accounts.models import UserAccount

class TipoFibra(models.Model):
    nombre = models.CharField(max_length=300)
    def __str__(self):
        return f'{self.nombre} '


class Fibra(models.Model):
    tipoFibra = models.ForeignKey(TipoFibra, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=300)
    numeroBuffers = models.IntegerField()
    numeroHilos = models.IntegerField()
    def __str__(self):
        return f'{self.tipoFibra} - {self.nombre} - b:{self.numeroBuffers} h:{self.numeroHilos}'


class Ruta(models.Model):
    nombre = models.CharField(max_length=300)
    fibra = models.ForeignKey(Fibra, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
class Buffer(models.Model):
    nombre = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre
    
class Hilo(models.Model):
    nombre = models.CharField(max_length=300)
    buffer= models.ForeignKey(Buffer, on_delete=models.CASCADE)
    fibra= models.ForeignKey(Fibra, on_delete=models.CASCADE) ####### MAL
    def __str__(self):
        return self.nombre
    
    
    