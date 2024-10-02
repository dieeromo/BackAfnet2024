from django.db import models
from accounts.models import UserAccount
from cliente.models import PlanClienteVivienda
from datetime import date, timedelta
from contabilidad.models import Caja
from decimal import Decimal

# Create your models here.

class QuejaCliente(models.Model):
    quejaCliente = models.TextField()
    prioridad = models.IntegerField(choices=[(1, 'Leve'), (2, 'Intermedio'), (3, 'Grave')], default=1)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    
class DiagnosticoPreliminar(models.Model):
    diagnosticoPreliminar= models.TextField()
    prioridad = models.IntegerField(choices=[(1, 'Leve'), (2, 'Intermedio'), (3, 'Grave')], default=1)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    
class DiagnosticoInSitu(models.Model):
    diagnosticoInSitu= models.TextField()
    prioridad = models.IntegerField(choices=[(1, 'Leve'), (2, 'Intermedio'), (3, 'Grave')], default=1)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    
class SolucionQuejaCliente(models.Model):
    solucion = models.TextField()
    dificultad = models.IntegerField(choices=[(1, 'Facil'), (2, 'Intermedia'), (3, 'Dificil')], default=1)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

    
class Mantenimiento(models.Model):
    planClienteVivienda = models.ForeignKey(PlanClienteVivienda,  on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_tentativa = models.DateField(null=True, blank=True)
    aclaracionVisita= models.TextField(null=True, blank=True)
    observacionGeneral= models.TextField(null=True, blank=True)
    
    queja_cliente = models.ForeignKey(QuejaCliente,  on_delete=models.CASCADE)
    otro_QuejaCliente = models.TextField(null=True, blank=True)
    
    diagnostico_preliminar = models.ForeignKey(DiagnosticoPreliminar,  on_delete=models.CASCADE)
    otro_DiagnosticoOficina = models.TextField(null=True, blank=True)
    
    diagnostico_InSitu = models.ForeignKey(DiagnosticoInSitu,  on_delete=models.CASCADE, null=True, blank=True)
    otro_DiagnosticoInSitu = models.TextField(null=True, blank=True)
    
    solucionPreliminar = models.ForeignKey(SolucionQuejaCliente,related_name='solucionPreliminar',  on_delete=models.CASCADE, null=True, blank=True)
    
    solucion = models.ForeignKey(SolucionQuejaCliente,  on_delete=models.CASCADE, null=True, blank=True)
    otra_solucion = models.TextField(null=True, blank=True)
    
    responsalibilad = models.IntegerField(choices=[(1, 'Empresa'), (2, 'Cliente'), (3, 'Otro')], default=1)
    
    fecha_solucion = models.DateTimeField(null=True, blank=True)
    
    digitador = models.ForeignKey(UserAccount, related_name='digitadorMantenimiento', on_delete=models.CASCADE)
    tecnico = models.ForeignKey(UserAccount,related_name='SolucionadorMantenimiento',  on_delete=models.CASCADE)
    
    
    
    
class SolicitudesCliente(models.Model):
    solicitudCliente = models.TextField()
    dificultad = models.IntegerField(choices=[(1, 'Facil'), (2, 'Intermedia'), (3, 'Dificil')], default=1)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

class RespuestasSolicitudesCliente(models.Model):
    respuestaCliente = models.TextField()
    dificultad = models.IntegerField(choices=[(1, 'Facil'), (2, 'Intermedia'), (3, 'Dificil')], default=1)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

class AtencionSolicitudesCliente(models.Model):
    planClienteVivienda = models.ForeignKey(PlanClienteVivienda,  on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_tentativa = models.DateField(null=True, blank=True)
    aclaracionVisita= models.TextField(null=True, blank=True)
    observacionGeneral= models.TextField(null=True, blank=True)
    
    solicitud_cliente = models.ForeignKey(SolicitudesCliente,  on_delete=models.CASCADE)
    otro_solicitudes = models.TextField(null=True, blank=True)
    
    respuesta_solicitud_cliente = models.ForeignKey(RespuestasSolicitudesCliente,  on_delete=models.CASCADE)
    otro_respuesta = models.TextField(null=True, blank=True)
    
    fecha_atencion = models.DateTimeField(null=True, blank=True)
    
    digitador = models.ForeignKey(UserAccount, related_name='digitadorSolicitud', on_delete=models.CASCADE)
    tecnico = models.ForeignKey(UserAccount,related_name='solucionadorSolicitud',  on_delete=models.CASCADE)
    
    