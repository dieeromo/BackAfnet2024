from django.db import models
from accounts.models import UserAccount
from .modelsCuarto import PuertoODF
from .modelsCajasMufas import CajaNap, Mufa


class TipoFibra(models.Model):
    nombre = models.CharField(max_length=300)
    def __str__(self):
        return f'{self.nombre} '
    
class CableFibra(models.Model):
    tipoFibra = models.ForeignKey(TipoFibra, on_delete=models.CASCADE)
    nombreRuta = models.CharField(max_length=300)
    numeroBuffers = models.IntegerField()
    numeroHilos = models.IntegerField()
    def __str__(self):
        return f'{self.tipoFibra} - b:{self.numeroBuffers} h:{self.numeroHilos}'
    
class HiloFibra(models.Model):
    hilo = models.IntegerField(choices=[(1, 'azul'), (2, 'tomate'), (3,'verde')], default=1)
    buffer = models.IntegerField(choices=[(1, 'azul'), (2, 'tomate'), (3,'verde')], default=1)
    cableFibra = models.ForeignKey(CableFibra,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.hilo} '
    
class Trazo1(models.Model): # es por donde pasa o es todo
    origen = models.ForeignKey(PuertoODF, on_delete=models.CASCADE)
    hilo = models.ForeignKey(HiloFibra, on_delete=models.CASCADE)
    
    mufa_destino = models.ForeignKey(Mufa, on_delete=models.CASCADE, null=True, blank=True)
    caja_destino = models.ForeignKey(CajaNap, on_delete=models.CASCADE, null=True, blank=True)
    
    conexion_splitter = models.IntegerField(choices=[(0, 'No'), (1, 'Si')], default=0)
    
    fecha_instalacion = models.DateField( null=True, blank=True )
    observacion = models.CharField(max_length=300,null=True, blank=True )
    verificado = models.IntegerField(choices=[(0, 'No'), (1, 'Si')], default=0)
    def __str__(self):
        return f'{self.hilo} '
    
class Trazo2(models.Model): # es por donde pasa o es todo
    origen = models.ForeignKey(Trazo1, on_delete=models.CASCADE)
    hilo = models.ForeignKey(HiloFibra, on_delete=models.CASCADE)
    
    mufa_destino = models.ForeignKey(Mufa, on_delete=models.CASCADE, null=True, blank=True)
    caja_destino = models.ForeignKey(CajaNap, on_delete=models.CASCADE, null=True, blank=True)
    
    conexion_splitter = models.IntegerField(choices=[(0, 'No'), (1, 'Si')], default=0)
    
    fecha_instalacion = models.DateField( null=True, blank=True )
    observacion = models.CharField(max_length=300,null=True, blank=True )
    verificado = models.IntegerField(choices=[(0, 'No'), (1, 'Si')], default=0)
    def __str__(self):
        return f'{self.hilo} '
    
class Trazo3(models.Model): # es por donde pasa o es todo
    origen = models.ForeignKey(Trazo2, on_delete=models.CASCADE)
    hilo = models.ForeignKey(HiloFibra, on_delete=models.CASCADE)
    
    mufa_destino = models.ForeignKey(Mufa, on_delete=models.CASCADE, null=True, blank=True)
    caja_destino = models.ForeignKey(CajaNap, on_delete=models.CASCADE, null=True, blank=True)
    
    conexion_splitter = models.IntegerField(choices=[(0, 'No'), (1, 'Si')], default=0)
    
    fecha_instalacion = models.DateField( null=True, blank=True )
    observacion = models.CharField(max_length=300,null=True, blank=True )
    verificado = models.IntegerField(choices=[(0, 'No'), (1, 'Si')], default=0)
    def __str__(self):
        return f'{self.hilo} '