from django.db import models
from accounts.models import UserAccount


class OLTNA(models.Model):
    nombre = models.CharField(max_length=300)
    fecha_instalacion = models.DateField( null=True, blank=True )
    
    def __str__(self):
        return self.nombre
    
class TarjetaOLTNA(models.Model):
    olt = models.ForeignKey(OLTNA, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=300)
    fecha_instalacion = models.DateField( null=True, blank=True )
    def __str__(self):
        return f'{self.olt} - {self.nombre} '
    
class PuertoTarjetaNA(models.Model):
    tarjeta = models.ForeignKey(TarjetaOLTNA ,on_delete=models.CASCADE)
    puerto = models.CharField(max_length=30)
    fecha_instalacion = models.DateField( null=True, blank=True )
    def __str__(self):
        return f'{self.tarjeta}  P:{self.puerto}'

class ODFNA(models.Model):
    nombre = models.CharField(max_length=300)
    fecha_instalacion = models.DateField( null=True, blank=True )
    def __str__(self):
        return f'{self.nombre} '
    
class PuertoODFNA(models.Model):
    odf = models.ForeignKey(ODFNA, on_delete=models.CASCADE)
    puerto = models.IntegerField()
    fecha_instalacion = models.DateField( null=True, blank=True )
    def __str__(self):
        return f'{self.odf} - P:{self.puerto}'

    
class TrazoPachcordNA(models.Model):
    sal_puertoTarjeta = models.ForeignKey(PuertoTarjetaNA, related_name='patchcors', on_delete=models.CASCADE)
    lleg_puertoODF = models.ForeignKey(PuertoODFNA, on_delete=models.CASCADE)
    
    comentario = models.CharField(max_length=300,null=True, blank=True )
    fecha_instalacion = models.DateField( null=True, blank=True )
    verificado = models.IntegerField(choices=[(1, 'No'), (2, 'Si')], default=1)
    def __str__(self):
        return f'{self.lleg_puertoODF} '
