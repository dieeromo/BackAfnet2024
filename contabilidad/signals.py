from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import PagoFacturasEquipos, PagoFacturasServicios, PagoFacturasVarios, PagoFacturasVehiculos
from .models import PagoPlanillaColaboradores, PagoPlanillaComisiones
from django.db.models import Sum



@receiver(post_save, sender=PagoFacturasEquipos)
def actualizar_factura_al_guardar_pago(sender, instance, **kwargs):
    factura = instance.facturaEquipos
    total_abonos = factura.pagosFacturaEquipos.aggregate(total_abono=Sum('abono'))['total_abono'] or 0
    factura.abono = total_abonos
    factura.actualizar_estado()

@receiver(post_delete, sender=PagoFacturasEquipos)
def actualizar_factura_al_eliminar_pago(sender, instance, **kwargs):
    factura = instance.facturaEquipos
    total_abonos = factura.pagosFacturaEquipos.aggregate(total_abono=Sum('abono'))['total_abono'] or 0
    factura.abono = total_abonos
    factura.actualizar_estado()
    
    
    
@receiver(post_save, sender=PagoFacturasServicios)
def actualizar_facturaServicio_al_guardar_pago(sender, instance, **kwargs):
    factura = instance.facturaServicios
    total_abonos = factura.pagosServicios.aggregate(total_abono=Sum('abono'))['total_abono'] or 0
    factura.abono = total_abonos
    factura.actualizar_estado()

@receiver(post_delete, sender=PagoFacturasServicios)
def actualizar_facturaServicios_al_eliminar_pago(sender, instance, **kwargs):
    factura = instance.facturaServicios
    total_abonos = factura.pagosServicios.aggregate(total_abono=Sum('abono'))['total_abono'] or 0
    factura.abono = total_abonos
    factura.actualizar_estado()
    
@receiver(post_save, sender=PagoFacturasVarios)
def actualizar_facturaVarios_al_guardar_pago(sender, instance, **kwargs):
    factura = instance.facturaVarios
    total_abonos = factura.pagosVarios.aggregate(total_abono=Sum('abono'))['total_abono'] or 0
    factura.abono = total_abonos
    factura.actualizar_estado()

@receiver(post_delete, sender=PagoFacturasVarios)
def actualizar_facturaVarios_al_eliminar_pago(sender, instance, **kwargs):
    factura = instance.facturaVarios
    total_abonos = factura.pagosVarios.aggregate(total_abono=Sum('abono'))['total_abono'] or 0
    factura.abono = total_abonos
    factura.actualizar_estado()
    
    
    #===========
@receiver(post_save, sender=PagoFacturasVehiculos)
def actualizar_facturaVehiculos_al_guardar_pago(sender, instance, **kwargs):
    factura = instance.facturaVehiculos
    total_abonos = factura.pagosVehiculos.aggregate(total_abono=Sum('abono'))['total_abono'] or 0
    factura.abono = total_abonos
    factura.actualizar_estado()

@receiver(post_delete, sender=PagoFacturasVehiculos)
def actualizar_facturaVehiculos_al_eliminar_pago(sender, instance, **kwargs):
    factura = instance.facturaVehiculos
    total_abonos = factura.pagosVehiculos.aggregate(total_abono=Sum('abono'))['total_abono'] or 0
    factura.abono = total_abonos
    factura.actualizar_estado()
    
    #===========
@receiver(post_save, sender=PagoPlanillaColaboradores)
def actualizar_planillaColaboradores_al_guardar_pago(sender, instance, **kwargs):
    factura = instance.planillaColaboradores
    total_abonos = factura.pagosPlanilla.aggregate(total_abono=Sum('abono'))['total_abono'] or 0
    factura.abono = total_abonos
    factura.actualizar_estado()

@receiver(post_delete, sender=PagoPlanillaColaboradores)
def actualizar_planillaColaboradores_al_eliminar_pago(sender, instance, **kwargs):
    factura = instance.planillaColaboradores
    total_abonos = factura.pagosPlanilla.aggregate(total_abono=Sum('abono'))['total_abono'] or 0
    factura.abono = total_abonos
    factura.actualizar_estado()
    
    #===========
@receiver(post_save, sender=PagoPlanillaComisiones)
def actualizar_planillaComisiones_al_guardar_pago(sender, instance, **kwargs):
    factura = instance.planillaComisiones
    total_abonos = factura.pagosPlanillaComisiones.aggregate(total_abono=Sum('abono'))['total_abono'] or 0
    factura.abono = total_abonos
    factura.actualizar_estado()

@receiver(post_delete, sender=PagoPlanillaComisiones)
def actualizar_planillaComisiones_al_eliminar_pago(sender, instance, **kwargs):
    factura = instance.planillaComisiones
    total_abonos = factura.pagosPlanillaComisiones.aggregate(total_abono=Sum('abono'))['total_abono'] or 0
    factura.abono = total_abonos
    factura.actualizar_estado()