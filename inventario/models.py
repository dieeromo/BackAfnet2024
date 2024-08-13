from django.db import models
from accounts.models import UserAccount
from cliente.models import PlanClienteVivienda
from contabilidad.models import FacturaEquipo

class TipoEquipo(models.Model):
    nombre = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre

class Homologado(models.Model):
    nombre = models.CharField(max_length=300)
    tipo = models.ForeignKey(TipoEquipo, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
class Bodega(models.Model):
    nombre = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre
    
class Equipo(models.Model):
    factura = models.ForeignKey(FacturaEquipo, related_name='equipos', on_delete=models.CASCADE, null=True, blank=True)
    homologado = models.ForeignKey(Homologado, on_delete=models.CASCADE)
    serie = models.CharField(max_length=300)
    precio_compra = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    estado = models.IntegerField(choices=[(1, 'Nuevo'), (2, 'Usado'), (3, 'Dañado')], default=1)
    estado2 = models.IntegerField(choices=[(1, 'No instalado'), (2, 'Instalado'), (3, 'Vendido')], default=1)
    fecha_ingreso = models.DateField( auto_now_add=True)
    observacion = models.CharField(max_length=300, null=True, blank=True)
    digitador =models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.homologado} - {self.serie}'
    def get_infoEquipo(self):
        return f'{self.homologado.nombre} - {self.serie} - {self.estado} - {self.bodega.nombre}'
    
    
    
    
class EquipoMovimientoBodega(models.Model):
    #factura
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    condicion = models.IntegerField(choices=[(1, 'Nuevo'), (2, 'Usado'), (3, 'Dañado')], null=True,blank=True)
    fecha_sistema = models.DateField( auto_now_add=True)
    fecha_ingreso = models.DateField( null=True, blank=True )
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=300, null=True, blank=True)
    digitador =models.ForeignKey(UserAccount, on_delete=models.CASCADE)
        
    def __str__(self):
        return f'{self.equipo} - Destino:{self.bodega} - {self.fecha_sistema}'
    
    
class EquipoInstalado(models.Model):
    #factura
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    planClienteVivienda = models.ForeignKey(PlanClienteVivienda,related_name='equipoInstalado', on_delete=models.CASCADE)
    fecha_instalacion = models.DateField( null=True, blank=True )

    motivo = models.IntegerField(choices=[(1, 'Instalacion'), (2, 'x Equipo dañado'), (3, 'x upgrade'),(4, 'Otro')], default=1)
    estado = models.IntegerField(choices=[(1, 'Activo'), (2, 'Pasivo'), (3, 'otro')], default=1)
    condicion = models.IntegerField(choices=[(1, 'Nuevo'), (2, 'Usado'), (3, 'Dañado')], null=True,blank=True)
    observacion = models.CharField(max_length=300, null=True, blank=True)
    digitador =models.ForeignKey(UserAccount, on_delete=models.CASCADE)
        
    def __str__(self):
        return f'{self.equipo} '
    def get_infoEquipo(self):
        return f'{self.equipo.homologado.nombre} {self.equipo.serie}'
    