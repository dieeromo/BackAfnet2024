from django.db import models
from accounts.models import UserAccount

class TipoFibraNA(models.Model):
    nombre = models.CharField(max_length=300)
    def __str__(self):
        return f'{self.nombre} '


class FibraNA(models.Model):
    tipoFibra = models.ForeignKey(TipoFibraNA, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=300)
    numeroBuffers = models.IntegerField()
    numeroHilos = models.IntegerField()
    def __str__(self):
        return f'{self.tipoFibra} - {self.nombre} - b:{self.numeroBuffers} h:{self.numeroHilos}'


class RutaNA(models.Model):
    nombre = models.CharField(max_length=300)
    fibra = models.ForeignKey(FibraNA, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
class BufferNA(models.Model):
    nombre = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre
    
class HiloNA(models.Model):
    nombre = models.CharField(max_length=300)
    buffer= models.ForeignKey(BufferNA, on_delete=models.CASCADE)
    fibra= models.ForeignKey(FibraNA, on_delete=models.CASCADE) ####### MAL
    def __str__(self):
        return self.nombre
    
    
    