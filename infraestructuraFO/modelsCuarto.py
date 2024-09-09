from django.db import models

# Create your models here.
class OLT(models.Model):
    nombre = models.CharField(max_length=300)
    fecha_instalacion = models.DateField( null=True, blank=True )
    
    def __str__(self):
        return self.nombre
    
class TarjetaOLT(models.Model):
    olt = models.ForeignKey(OLT, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=300)
    fecha_instalacion = models.DateField( null=True, blank=True )
    def __str__(self):
        return f'{self.olt} - {self.nombre} '
    
class PuertoTarjeta(models.Model):
    tarjeta = models.ForeignKey(TarjetaOLT ,on_delete=models.CASCADE)
    puerto = models.CharField(max_length=30)
    fecha_instalacion = models.DateField( null=True, blank=True )
    def __str__(self):
        return f'{self.tarjeta}  P:{self.puerto}'

class ODF(models.Model):
    nombre = models.CharField(max_length=300)
    fecha_instalacion = models.DateField( null=True, blank=True )
    def __str__(self):
        return f'{self.nombre} '
    
class PuertoODF(models.Model):
    odf = models.ForeignKey(ODF, on_delete=models.CASCADE)
    puerto = models.IntegerField()
    fecha_instalacion = models.DateField( null=True, blank=True )
    def __str__(self):
        return f'{self.puerto}'

    
class TrazoPachcord(models.Model):
    sal_puertoTarjeta = models.ForeignKey(PuertoTarjeta, on_delete=models.CASCADE)
    lleg_puertoODF = models.ForeignKey(PuertoODF, on_delete=models.CASCADE)
    
    observacion = models.CharField(max_length=300,null=True, blank=True )
    fecha_instalacion = models.DateField( null=True, blank=True )
    verificado = models.IntegerField(choices=[(1, 'No'), (2, 'Si')], default=1)
    def __str__(self):
        return f'{self.lleg_puertoODF} '
