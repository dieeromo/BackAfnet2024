# models.py

from django.db import models
from django.db.models import Sum
from accounts.models import UserAccount
from decimal import Decimal


class TipoInstitucion(models.Model):
    nombre = models.CharField(max_length=150)
    def __str__(self):
        return self.nombre
    
class Institucion(models.Model):
    tipo = models.ForeignKey(TipoInstitucion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    def __str__(self):
        return self.nombre


class Inversion(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    valor_inversion = models.DecimalField(max_digits=10, decimal_places=2)
    porcentajeRendimiento = models.DecimalField(max_digits=5, decimal_places=2)
    valorRendimiento = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_emision = models.DateField()
    fecha_caduca = models.DateField()
    estado_diversificacion = models.BooleanField(default=False)
    propierario = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    porcentaje_retiro = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    valor_retiro = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    estado_inversion = models.IntegerField(choices=[(1, 'Activa'), (2, 'Pasiva'), (3, 'Retirada')], default=1)
    
    def save(self, *args, **kwargs):
        # super().save(*args, **kwargs)
        # if self.diversificaciones.aggregate(Sum('valor_inversion'))['valor_inversion__sum'] == self.valor_inversion:
        #     self.estado_diversificacion = True
        # else:
        #     self.estado_diversificacion = False
        super().save(*args, **kwargs)
        if self.valor_retiro >= self.valor_inversion:
            self.estado_inversion = 3
        if self.valor_inversion > 0:
            self.porcentaje_retiro = (self.valor_retiro / self.valor_inversion) * 100
        super().save(*args, **kwargs)
        
class Destino(models.Model):
    nombre = models.CharField(max_length=150)
    def __str__(self):
        return self.nombre


class Diversificacion(models.Model):
    inversion = models.ForeignKey(Inversion, related_name='diversificaciones', on_delete=models.CASCADE)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    valor_inversion = models.DecimalField(max_digits=10, decimal_places=2)
    valor_rendimiento = models.DecimalField(max_digits=10, decimal_places=2)

    #def __str__(self):
    #    return self.inversion


class SubDestino(models.Model):
    nombre = models.CharField(max_length=150)
    # def __str__(self):
    #     return self.nombre
    
    
class Retiro(models.Model):
    diversificacion = models.ForeignKey(Diversificacion, related_name='retiros', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    subDestino = models.ForeignKey(SubDestino, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        inversion = self.diversificacion.inversion
        inversion.valor_retiro += Decimal(self.valor)
        inversion.save()
        super().save(*args, **kwargs)
    def __str__(self):
        return f'Retiro {self.descripcion}'