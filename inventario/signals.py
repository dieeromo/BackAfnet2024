from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Equipo, EquipoMovimientoBodega, EquipoInstalado
from cliente.models import PlanClienteVivienda
#Actualizar en tabla Equipo cuando se hace una entrada en Equipo Instalado
# @receiver(pre_save, sender=EquipoInstalado)
# def actualizar_estado2_equipo(sender, instance, **kwargs):
#     if instance.pk:
#         previous = EquipoInstalado.objects.get(pk=instance.pk)

#         if (previous.estado == 1) and (instance.estado == 2):

#             equipo = instance.equipo
#             equipo.estado2 = '1'
#             equipo.save()

#Cuando se hace una entrada en EquipoInstalado se modifica el estado en Equipo
@receiver(post_save, sender=EquipoInstalado)
def actualizar_estado_equipo(sender, instance, created, **kwargs):
    if created:
        equipo = instance.equipo
        equipo.estado2 = '2'
        
        equipo.save()
        
#Cuando se le cambia de bodega en Equipo se hace una entrada EquipoMovimientoBodega
@receiver(pre_save, sender=Equipo)
def registrarMovimientoBodega(sender, instance, **kwargs):
    if instance.pk:
        # Obtenemos la instancia anterior del equipo
        equipo_anterior = Equipo.objects.get(pk=instance.pk)
        if equipo_anterior.bodega != instance.bodega:
            # Registrar el cambio en el histórico
            EquipoMovimientoBodega.objects.create(
                equipo=instance,
                bodega=instance.bodega,
                condicion=instance.estado,
                digitador=instance.digitador
            )


        
##### Se crea una entrada en MovimientoEquipo cuando se hace una entrada en Equipo
@receiver(post_save, sender=Equipo)
def create_equipo_movimiento_bodega(sender, instance, created, **kwargs):
    if created:
        EquipoMovimientoBodega.objects.create(
            equipo=instance,
            fecha_ingreso=instance.fecha_ingreso,
            bodega=instance.bodega,
            condicion=instance.estado,
            observacion=instance.observacion,
            digitador=instance.digitador
       )
        
######## para actualizar la tabla Equipo cuando se modifique el estado en la tabla EquipoInstalado
@receiver(post_save, sender=EquipoInstalado)
def update_equipo_estado2(sender, instance, **kwargs):
    if instance.estado == 2:  # 2 means 'Pasivo'
        equipo = instance.equipo
        equipo.estado2 = 1  # 1 means 'No instalado'
        equipo.estado = 2  # 1 means 'No instalado'
        equipo.save()
        
        
        
###señal para cambiar el estado de quipo instalado a pasivo cuando se da de baja un plan
        
@receiver(pre_save, sender=PlanClienteVivienda)
def update_equipo_instalado_estado(sender, instance, **kwargs):
    if instance.pk:  # Check if it's an update
        try:
            previous = PlanClienteVivienda.objects.get(pk=instance.pk)
        except PlanClienteVivienda.DoesNotExist:
            previous = None

        if previous and previous.estado == 1 and instance.estado == 5:
            # Get all related EquipoInstalado objects and update their estado to 'Pasivo'
            EquipoInstalado.objects.filter(planClienteVivienda=instance).update(estado=2)


###para actualizar la Tabla Equipo cuando cambia
@receiver(pre_save, sender=EquipoInstalado)
def update_equipo_estado2(sender, instance, **kwargs):
    if instance.pk:  # Check if it's an update
        try:
            previous = EquipoInstalado.objects.get(pk=instance.pk)
        except EquipoInstalado.DoesNotExist:
            previous = None

        if previous and previous.estado == 1 and instance.estado == 2:
            # Update the estado2 of the related Equipo to 'No instalado'
            instance.equipo.estado2 = 1  # Assuming 1 is 'No instalado'
            instance.equipo.save()
