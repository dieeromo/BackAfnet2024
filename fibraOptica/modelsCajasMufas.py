from django.db import models
from cliente.models import Barrio, Comunidad




class MufaNA(models.Model):
    barrio = models.ForeignKey(Barrio,blank=True, null=True, on_delete=models.CASCADE)
    comunidad = models.ForeignKey(Comunidad, blank=True, null=True, on_delete=models.CASCADE)
    numero = models.IntegerField()
    splitter = models.IntegerField(null=True, blank=True)
    potencia = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    coordenadas = models.CharField(max_length=300, null=True, blank=True)
    observacion = models.CharField(max_length=300, null=True, blank=True)
    fecha_instalacion = models.DateField( null=True, blank=True )
    verificado = models.IntegerField(choices=[(1, 'No'), (2, 'Si')], default=1)
    def __str__(self):
        return f'mufa:{self.numero} - dir:{self.barrio}{self.comunidad}'
    
    
class CajaNapNA(models.Model):
    mufa = models.ForeignKey(MufaNA, on_delete=models.CASCADE)
    barrio = models.ForeignKey(Barrio,blank=True, null=True, on_delete=models.CASCADE)
    comunidad = models.ForeignKey(Comunidad, blank=True, null=True, on_delete=models.CASCADE)
    
    numeroNap = models.IntegerField()
    nombreNap = models.CharField(max_length=300, null=True, blank=True)
    splitter = models.IntegerField(null=True, blank=True)
    
    puertos = models.IntegerField(null=True, blank=True)
    puertosDanados = models.IntegerField(default=0)
    potencia = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    fecha_instalacion = models.DateField( null=True, blank=True )
    
    coordenadas = models.CharField(max_length=300, null=True, blank=True)
    observacion = models.CharField(max_length=300, null=True, blank=True)
    verificado = models.IntegerField(choices=[(1, 'No'), (2, 'Si')], default=1)
    
    def __str__(self):
        return f'nap:{self.numeroNap} - #pu:{self.puertos} - {self.fecha_instalacion}'