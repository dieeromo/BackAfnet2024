from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import ClienteVivienda, ClienteViviendaHistorico, PlanClienteVivienda, Upgrade
from .models import Cliente, OrdenInstalacion, OrdenCobro, PagosPlanClienteVivienda
from decimal import Decimal
from django.db.models import Sum

@receiver(post_save, sender=OrdenInstalacion)
def create_Cliente(sender, instance, **kwargs):
    if instance.estado == 2:
        Cliente.objects.get_or_create(
            ordenInstalacion=instance,
            nombresApellidos=instance.nombresApellidos,
            cedula = instance.cedula,
            telefono1 = instance.telefono1,
            tipoCliente = instance.tipoCliente,
            nacionalidadCliente = instance.nacionalidadCliente,
            digitador = instance.digitador
        )
        
@receiver(post_save, sender=PlanClienteVivienda)
def create_upgrade(sender, instance, created, **kwargs):
    Upgrade.objects.create(
        planClienteVivienda=instance,
        plan_upgrade=instance.plan,
        fecha=instance.fecha_instalacion,
    )
    if not created:
        Upgrade.objects.create(
            planClienteVivienda=instance,
            plan_upgrade=instance.plan,
            fecha=instance.fecha_instalacion,
        )
######


###############################
# @receiver(pre_save, sender=PlanClienteVivienda)
# def check_plan_upgrade_change(sender, instance, **kwargs):
#     if instance.pk:
#         old_instance = PlanClienteVivienda.objects.get(pk=instance.pk)
#         if old_instance.plan != instance.plan:
#             instance.plan_changed = True
#         else:
#             instance.plan_changed = False

# @receiver(post_save, sender=PlanClienteVivienda)
# def create_or_update_upgrade(sender, instance, created, **kwargs):
#     if created:
#         Upgrade.objects.create(
#             planClienteVivienda=instance,
#             plan_upgrade=instance.plan,
#             fecha=instance.fecha_instalacion,
#         )
#     else:
#         if hasattr(instance, 'plan_changed') and instance.plan_changed:
#             Upgrade.objects.create(
#                 planClienteVivienda=instance,
#                 plan_upgrade=instance.plan,
#                 fecha=instance.fecha_instalacion,
#             )
#         else:
#             Upgrade.objects.update_or_create(
#                 planClienteVivienda=instance,
#                 defaults={
#                     'plan_upgrade': instance.plan,
#                     'fecha': instance.fecha_instalacion,
#                 }
#            )

###############

# @receiver(pre_save, sender=PlanClienteVivienda)
# def check_plan_upgrade_change(sender, instance, **kwargs):
#     if instance.pk:
#         old_instance = PlanClienteVivienda.objects.get(pk=instance.pk)
#         # Check if the plan has changed
#         if old_instance.plan != instance.plan:
#             instance.plan_changed = True
#         else:
#             instance.plan_changed = False
#     else:
#         instance.plan_changed = False

# @receiver(post_save, sender=PlanClienteVivienda)
# def create_or_update_upgrade(sender, instance, created, **kwargs):
#     if created:
#         Upgrade.objects.create(
#             planClienteVivienda=instance,
#             plan_upgrade=instance.plan,
#             fecha=instance.fecha_instalacion,
#         )
#     else:
#         if hasattr(instance, 'plan_changed') and instance.plan_changed:
#             Upgrade.objects.create(
#                 planClienteVivienda=instance,
#                 plan_upgrade=instance.plan,
#                 fecha=instance.fecha_instalacion,
#             )

# # Handle updates separately to ensure only the correct fields are monitored
# @receiver(pre_save, sender=PlanClienteVivienda)
# def update_upgrade_on_change(sender, instance, **kwargs):
#     if instance.pk:
#         old_instance = PlanClienteVivienda.objects.get(pk=instance.pk)
#         # Only update Upgrade if plan has changed
#         if old_instance.plan != instance.plan:
#             Upgrade.objects.update_or_create(
#                 planClienteVivienda=instance,
#                 defaults={
#                     'plan_upgrade': instance.plan,
#                     'fecha': instance.fecha_instalacion,
#                 }
#             )


########################




@receiver(post_save, sender=ClienteVivienda)
def create_cliente_vivienda_historico(sender, instance, created, **kwargs):
    ClienteViviendaHistorico.objects.create(
        clienteVivienda=instance,
        cliente=instance.cliente,
        vivienda=instance.vivienda,
        fecha_inicio=instance.fecha_inicio,
        digitador = instance.digitador
    )
    
    if not created:
        ClienteViviendaHistorico.objects.create(
            clienteVivienda=instance,
            cliente=instance.cliente,
            vivienda=instance.vivienda,
            fecha_inicio=instance.fecha_inicio,
            fecha_fin=instance.fecha_fin,
            digitador = instance.digitador
        )


#### SIGNAS PARA PAGOS DE CLIENTES

@receiver(post_save, sender=PagosPlanClienteVivienda)
@receiver(post_delete, sender=PagosPlanClienteVivienda)
def actualizar_valor_abonado(sender, instance, **kwargs):
    orden = instance.orden_cobro
    total_abonado = orden.pagosPlanClienteVivienda.aggregate(total_abonos=Sum('total_abono'))['total_abonos'] or 0
    orden.valor_abonado = total_abonado
    
    # Actualizar el estado de la orden de cobro si ha sido pagada completamente
    if orden.valor_abonado >= orden.valor_total:
        orden.estado = 3  # Pagada
    else:
        orden.estado = 1  # Pendiente, si no ha sido completamente pagada
    
    orden.save()
