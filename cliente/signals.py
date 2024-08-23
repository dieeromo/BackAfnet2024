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
        
        
### para el upgrade
@receiver(pre_save, sender=PlanClienteVivienda)
def obtener_plan_anterior(sender, instance, **kwargs):
    if instance.pk:
        # Obtener el plan actual antes de que se guarde la instancia
        instance._plan_anterior = PlanClienteVivienda.objects.get(pk=instance.pk).plan
    else:
        instance._plan_anterior = None

@receiver(post_save, sender=PlanClienteVivienda)
def crear_upgrade(sender, instance, created, **kwargs):
    print('signalssssssssss sss  sss sss sss')
    if created:
        # Si la entrada es nueva (es decir, se acaba de crear)
        Upgrade.objects.create(
            planClienteVivienda=instance,
            plan_upgrade=instance.plan,
            fecha=instance.fecha_instalacion
        )
    else:
        # Si la entrada ya existía y se actualiza
        previous_plan = PlanClienteVivienda.objects.get(pk=instance.pk).plan
        print('instance plan', instance.plan)
        print('previos plan', instance._plan_anterior)
        if instance.plan != instance._plan_anterior:
            print('si ingresa a crear')
            Upgrade.objects.create(
                planClienteVivienda=instance,
                plan_upgrade=instance.plan,
                fecha=instance.fecha_instalacion
            )


###############################




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
