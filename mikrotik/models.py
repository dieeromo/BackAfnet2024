from django.db import models
from inventario.models import EquipoInstalado
from cliente.models import PlanClienteVivienda

from django.contrib.auth.hashers import make_password, check_password

class RouterMK(models.Model):
    nombre = models.CharField(max_length=100)
    router_instalado = models.ForeignKey(EquipoInstalado, on_delete=models.CASCADE)
    # Campo para almacenar la dirección IPv4
    ipv4_address = models.GenericIPAddressField(protocol='IPv4', null=True, blank=True)  
    # Campo para almacenar la dirección IPv6
    ipv6_address = models.GenericIPAddressField(protocol='IPv6', null=True, blank=True)  
    puerto = models.IntegerField(null=True, blank=True)
    usuario = models.CharField(max_length=50,null=True, blank=True)
    contrasena = models.CharField(max_length=128, null=True, blank=True)  # Usamos un campo más largo para almacenar la contraseña cifrada
    observacion = models.TextField(null=True, blank=True)
    def __str__(self):
        return f'{self.nombre} - IPv4: {self.ipv4_address} - IPv6: {self.ipv6_address}'


class AP_nodos(models.Model):
    router = models.ForeignKey(RouterMK,related_name='apodos', null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    ap_instalado = models.ForeignKey(EquipoInstalado, on_delete=models.CASCADE)
    ssid = models.CharField(max_length=100)
    frecuencia = models.IntegerField()
    
    ipv4_address = models.GenericIPAddressField(protocol='IPv4',  null=True, blank=True)  
    # Campo para almacenar la dirección IPv6
    ipv6_address = models.GenericIPAddressField(protocol='IPv6', null=True, blank=True)  
    puerto = models.IntegerField( null=True, blank=True)
    usuario = models.CharField(max_length=50, null=True, blank=True)
    contrasena = models.CharField(max_length=128, null=True, blank=True)  # Usamos un campo más largo para almacenar la contraseña cifrada
    observacion = models.TextField(null=True, blank=True)
    def __str__(self):
        return f'{self.nombre} - {self.router}'


    
    
    
from infraestructuraFO.modelsCajasMufas import CajaNap
class Mikrotik_PlanClienteVivienda(models.Model):
    planCliente = models.ForeignKey(PlanClienteVivienda, on_delete=models.CASCADE)
    ap = models.ForeignKey(AP_nodos, null=True, blank=True, on_delete=models.CASCADE)
    caja = models.ForeignKey(CajaNap, null=True, blank=True, on_delete=models.CASCADE)
    # Campo para almacenar la dirección IPv4
    ipv4_address = models.GenericIPAddressField(protocol='IPv4',  null=True, blank=True)  
    # Campo para almacenar la dirección IPv6
    ipv6_address = models.GenericIPAddressField(protocol='IPv6', null=True, blank=True) 
    
    puerto = models.IntegerField(null=True, blank=True)   # puerto de conexion a la antena
    usuario = models.CharField(max_length=50, null=True, blank=True)
    contrasena = models.CharField(max_length=128, null=True, blank=True)  # Usamos un campo más largo para almacenar la contraseña cifrada
    observacion = models.TextField(null=True, blank=True)
    



