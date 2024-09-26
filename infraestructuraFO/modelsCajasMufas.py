from django.db import models
from cliente.models import Barrio, Comunidad
from .modelsCuarto import PuertoTarjeta




class Mufa(models.Model):

    numero = models.IntegerField(null=True, blank=True)
    splitter = models.IntegerField(null=True, blank=True)
    splitter_adicional = models.IntegerField(null=True, blank=True)
    potencia = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
   
    fecha_instalacion = models.DateField( null=True, blank=True )
    observacion = models.CharField(max_length=300, null=True, blank=True)
    
    barrio = models.ForeignKey(Barrio,blank=True, null=True, on_delete=models.CASCADE)
    comunidad = models.ForeignKey(Comunidad, blank=True, null=True, on_delete=models.CASCADE)
    coordenadas = models.CharField(max_length=300, null=True, blank=True)
    
    verificado = models.IntegerField(choices=[(0, 'No'), (1, 'Si')], default=0)
    puerto_olt = models.ForeignKey(PuertoTarjeta,null=True, blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.numero}'

    
    
class CajaNap(models.Model):
    mufa = models.ForeignKey(Mufa,  related_name='cajasNap',on_delete=models.CASCADE)
    
    numeroNap = models.IntegerField(null=True, blank=True)
    nombreNap = models.CharField(max_length=50, null=True, blank=True)
    splitter = models.IntegerField(null=True, blank=True)
    splitter_adicional = models.IntegerField(null=True, blank=True)
    
    puertos = models.IntegerField(null=True, blank=True)
    puertosDanados = models.IntegerField(default=0)
    potencia = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    fecha_instalacion = models.DateField( null=True, blank=True )
    
    observacion = models.CharField(max_length=300, null=True, blank=True)
    
    barrio = models.ForeignKey(Barrio,blank=True, null=True, on_delete=models.CASCADE)
    comunidad = models.ForeignKey(Comunidad, blank=True, null=True, on_delete=models.CASCADE)
    coordenadas = models.CharField(max_length=300, null=True, blank=True)
    
    verificado = models.IntegerField(choices=[(0, 'No'), (1, 'Si')], default=0)
    
    # def __str__(self):
    #     return f'nap:{self.numeroNap} - #pu:{self.puertos} - {self.fecha_instalacion}'
    
    
    

