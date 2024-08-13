from django.db import models
from accounts.models import UserAccount

# Create your models here.

class TipoCliente(models.Model):
    nombre = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre
    
class NacionalidadCliente(models.Model):
    nombre = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre
    
class Ciudad(models.Model):
    nombre = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre
    
class Barrio(models.Model):
    nombre = models.CharField(max_length=300)
    ciudad = models.ForeignKey(Ciudad, related_name='barrios', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    def get_full_barrio(self):
        return "{} - {}".format(self.nombre, self.ciudad) 

class Comunidad(models.Model):
    nombre = models.CharField(max_length=300)
    ciudad = models.ForeignKey(Ciudad, related_name='comunidades', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
class OrdenInstalacion(models.Model):
    nombresApellidos = models.CharField(max_length=300)
    cedula = models.CharField(max_length=30,null=True, blank=True)
    telefono1 = models.CharField(max_length=30, null=True, blank=True)
    telefono2 = models.CharField(max_length=30, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    tipoCliente = models.ForeignKey(TipoCliente,  on_delete=models.CASCADE)
    tipoInstalacion = models.IntegerField(choices=[(1, 'Normal'), (2, 'Cambio operadora'), ], default=1)
    nacionalidadCliente = models.ForeignKey(NacionalidadCliente,  on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    observacion = models.CharField(max_length=300, null=True, blank=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    estado = models.IntegerField(choices=[(1, 'No Instalado'), (2, 'Instalado'), (3, 'Eliminado')], default=1)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nombresApellidos} - {self.cedula} desde {self.direccion}'
    

class Cliente(models.Model):
    ordenInstalacion =  models.ForeignKey(OrdenInstalacion,  on_delete=models.CASCADE, null=True, blank=True)
    nombresApellidos = models.CharField(max_length=300)
    cedula = models.CharField(max_length=30, null=True, blank=True)
    telefono1 = models.CharField(max_length=30, null=True, blank=True)
    telefono2 = models.CharField(max_length=30,  null=True, blank=True)
    email = models.CharField(max_length=50,  null=True, blank=True)
    tipoCliente = models.ForeignKey(TipoCliente,  on_delete=models.CASCADE)
    nacionalidadCliente = models.ForeignKey(NacionalidadCliente,  on_delete=models.CASCADE)
    observacion = models.CharField(max_length=300,  null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombresApellidos
    
    
class Vivienda(models.Model):
    barrio = models.ForeignKey(Barrio, related_name='vivienda',blank=True, null=True, on_delete=models.CASCADE)
    comunidad = models.ForeignKey(Comunidad, blank=True, null=True, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=300)
    coordenadas = models.CharField(max_length=100)  
    digitador = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_vivienda/', blank=True, null=True)
    
    def get_vivienda(self):
        return "{} - {} - {}".format(self.barrio, self.comunidad, self.direccion) 
    def __str__(self):
        return f'V{self.id} - {self.barrio} - {self.comunidad} - {self.direccion}'
    

    
    
class ClienteVivienda(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='clienteviviendas',  on_delete=models.CASCADE)
    vivienda = models.ForeignKey(Vivienda,  on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)

    tipo = models.IntegerField(choices=[(1, 'Propia'), (2, 'Arrendada'), (3, 'Otro')], default=1)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE) 
  
    def __str__(self):
        return f'CV:{self.id} {self.cliente.nombresApellidos} - V{self.vivienda.id} - desde:{self.fecha_inicio} hasta {self.fecha_fin}'
    
class ClienteViviendaHistorico(models.Model):
    clienteVivienda = models.ForeignKey(ClienteVivienda,   on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente,   on_delete=models.CASCADE)
    vivienda = models.ForeignKey(Vivienda,  on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE) 
  
    def __str__(self):
        return f'CV:{self.clienteVivienda.id} {self.cliente} - V{self.vivienda.id} - desde:{self.fecha_inicio} hasta {self.fecha_fin}'
    
    
class Plan(models.Model):
    nombre = models.CharField(max_length=300)
    valor= models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.nombre
    

    

class PlanClienteVivienda(models.Model):
    #ORDEN INSTALACION
    clienteVivienda = models.ForeignKey(ClienteVivienda,  on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan,  on_delete=models.CASCADE)
    fecha_instalacion = models.DateField()
    fecha_pago = models.DateField()
    estado = models.IntegerField(choices=[(1, 'Activo'), (2, 'Suspendido'), (3, 'Cortado'),(4, 'CambioPlan'),(5, 'Retirado')], default=1)
    
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE) 
  
    def __str__(self):
        return f'PCV:{self.id} {self.clienteVivienda.cliente.nombresApellidos} - V{self.clienteVivienda.vivienda.id} - {self.plan} desde {self.fecha_instalacion}'
    
    
class Upgrade(models.Model):
    planClienteVivienda = models.ForeignKey(PlanClienteVivienda,  on_delete=models.CASCADE)
    plan_upgrade = models.ForeignKey(Plan,  on_delete=models.CASCADE)
    fecha= models.DateField()

    def __str__(self):
        return f'U:{self.id} PCV:{self.planClienteVivienda.id} - {self.planClienteVivienda.clienteVivienda.cliente.nombresApellidos} - CV{self.planClienteVivienda.clienteVivienda.id} - {self.plan_upgrade} desde {self.fecha}'



