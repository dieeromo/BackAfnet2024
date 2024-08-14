from django.db import models
from accounts.models import UserAccount
from datetime import date, timedelta
from contabilidad.models import Caja
from decimal import Decimal

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
    alias = models.CharField(max_length=300, null=True, blank=True)
    valor= models.FloatField()
    def __str__(self):
        return self.nombre
    

    

class PlanClienteVivienda(models.Model):
    #ORDEN INSTALACION
    clienteVivienda = models.ForeignKey(ClienteVivienda,  on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan,  on_delete=models.CASCADE)
    fecha_instalacion = models.DateField()
    fecha_desinstalacion = models.DateField(blank=True, null=True)
    fecha_pago = models.DateField()
    estado = models.IntegerField(choices=[(1, 'Activo'), (2, 'Suspendido'),(3, 'Retirado'),(4, 'Upgrade')], default=1)
    estadoServicio = models.IntegerField(choices=[(1, 'Corriendo'), (2, 'Cortado')], default=1)
    estadoEquipos = models.IntegerField(choices=[(1, 'Funcionando'), (2, 'Por retirar'), (3, 'Retirados'),(4, 'Reseteados por retirados'),], default=1)
    #Activo: estado normal
    #Suspendido: Cuando el cliente suspende por un par de meses
    #Cortado: Cuando el cliente se retrasa de pagar
    
    digitador = models.ForeignKey(UserAccount, on_delete=models.CASCADE) 
  
    def __str__(self):
        return f'PCV:{self.id} {self.clienteVivienda.cliente.nombresApellidos} - V{self.clienteVivienda.vivienda.id} - {self.plan} desde {self.fecha_instalacion}'
    
    
class Upgrade(models.Model):
    planClienteVivienda = models.ForeignKey(PlanClienteVivienda,  on_delete=models.CASCADE)
    plan_upgrade = models.ForeignKey(Plan,  on_delete=models.CASCADE)
    fecha= models.DateField()

    def __str__(self):
        return f'U:{self.id} PCV:{self.planClienteVivienda.id} - {self.planClienteVivienda.clienteVivienda.cliente.nombresApellidos} - CV{self.planClienteVivienda.clienteVivienda.id} - {self.plan_upgrade} desde {self.fecha}'

#########################
class OrdenCobro(models.Model):
    planClienteVivienda = models.ForeignKey(PlanClienteVivienda, on_delete=models.CASCADE)
    fecha_generacion = models.DateField()
    fecha_gen_sis = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_vencimiento = models.DateField()
    valor_subtotal = models.FloatField()
    valor_iva = models.FloatField()
    valor_total = models.FloatField()
    valor_abonado = models.FloatField( default=0)  # Nuevo campo para abonos
    estado = models.IntegerField(choices=[(1, 'Pendiente'), (2, 'Vencida'), (3, 'Pagada')], default=1)
    dias_extras = models.IntegerField(default=0, help_text="Días extras despues del vencimiento, si no se corta automaticamente")
    ejecucion_dias_extras = models.IntegerField(choices=[(1, 'No Cortar'), (2, 'Cortar')], default=1)
    
    def __str__(self):
        return f'Orden de Cobro #{self.id} - PCV:{self.planClienteVivienda.id}'

    def calcular_valores(self):
        if self.planClienteVivienda.estado == 1 and self.planClienteVivienda.estadoServicio == 1:

            self.valor_subtotal = self.planClienteVivienda.plan.valor
            self.valor_iva = self.valor_subtotal * 0.15  # Supone un IVA del 15%
            self.valor_total = float(self.valor_subtotal + self.valor_iva)
        else:
            self.valor_subtotal = 0
            self.valor_iva = 0
            self.valor_total = 0
        self.save()
        
    def actualizar_abono(self, abono):
        self.valor_abonado += abono
        if self.valor_abonado >= self.valor_total:
            self.estado = 3  # Pagada
        else:
            self.estado = 1  # Pendiente
        self.save()



    @staticmethod
    def generar_ordenes_de_cobro():
        hoy = date.today()
        primer_dia_mes = hoy.replace(day=1)
        fecha_vencimiento = primer_dia_mes + timedelta(days=9)
        plan_cliente_viviendas = PlanClienteVivienda.objects.filter(estado=1, estadoServicio=1)
        
        for pcv in plan_cliente_viviendas:
            orden = OrdenCobro(
                planClienteVivienda=pcv,
                fecha_generacion=primer_dia_mes,
                fecha_vencimiento=fecha_vencimiento,
            )
            orden.calcular_valores()
            orden.save()
    
    @staticmethod
    def actualizar_estados_de_ordenes():
        ordenes = OrdenCobro.objects.filter(estado=1)
        hoy = date.today()
        
        for orden in ordenes:
            if hoy > (orden.fecha_vencimiento + timedelta(days=orden.dias_extras)):
                orden.estado = 2  # Vencida
                orden.save()



class PagosPlanClienteVivienda(models.Model):
    orden_cobro = models.ForeignKey(OrdenCobro,related_name='pagosPlanClienteVivienda' , on_delete=models.CASCADE)
    caja = models.ForeignKey(Caja, on_delete=models.CASCADE)
    fecha_pago = models.DateField()

    subtotal_abono = models.FloatField()
    iva_abono = models.FloatField()
    total_abono = models.FloatField()
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Pago #{self.id} - OrdenCobro:{self.orden_cobro.id} - Abono: {self.total_abono}'

 