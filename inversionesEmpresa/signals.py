from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Diversificacion, Inversion
from django.db.models import Sum

@receiver(post_save, sender=Diversificacion)
@receiver(post_delete, sender=Diversificacion)
def actualizar_estado_diversificacion(sender, instance, **kwargs):
    inversion = instance.inversion
    total_porcentaje = Diversificacion.objects.filter(inversion=inversion).aggregate(Sum('porcentaje'))['porcentaje__sum'] or 0

    if total_porcentaje == 100:
        inversion.estado_diversificacion = True
    else:
        inversion.estado_diversificacion = False

    inversion.save()
