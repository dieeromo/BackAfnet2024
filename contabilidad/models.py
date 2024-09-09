from django.db import models
from accounts.models import UserAccount

# Create your models here.
class Caja(models.Model):
    nombre = models.CharField(max_length=300)
    usuario = models.ForeignKey(UserAccount,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
class ProveedorEquipo(models.Model):
    nombre = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre
    
class ModoCompra(models.Model):
    nombre = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre
    
class ModoPagoProveedor(models.Model):
    nombre = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre
    

class Presupuesto(models.Model):
    nombre = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre
    
class FacturaEquipo(models.Model):
    proveedor = models.ForeignKey(ProveedorEquipo,  on_delete=models.CASCADE)
    fecha_emision= models.DateField()
    numeroFactura = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    abono= models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pagado = models.BooleanField(default=False)
    
    modoCompra = models.ForeignKey(ModoCompra,  on_delete=models.CASCADE)
    inventario = models.BooleanField(default=True)
    equiposIngresados = models.BooleanField(default=False)
    
    presupuesto = models.ForeignKey(Presupuesto,  on_delete=models.CASCADE)
    digitador = models.ForeignKey(UserAccount,  on_delete=models.CASCADE)
    observacion = models.CharField(max_length=300, null=True, blank=True)
    
    def actualizar_estado(self):
        self.pagado = self.abono >= self.valor
        self.save()
        
    def __str__(self):
        return f'{self.proveedor} - {self.fecha_emision} desde {self.descripcion}'
    def get_inventario(self):
        if self.inventario:
            return f'si'
        else:
            return f'no'
    def get_equiposIngresados(self):
        if self.equiposIngresados:
            return f'si'
        else:
            return f'no'    

class PagoFacturasEquipos(models.Model):
    facturaEquipos = models.ForeignKey(FacturaEquipo, related_name='pagosFacturaEquipos' ,on_delete=models.CASCADE)
    abono = models.DecimalField(max_digits=10, decimal_places=2)
    caja = models.ForeignKey(Caja,  on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    observacion = models.CharField(max_length=300, null=True, blank=True)
    modoPago = models.ForeignKey(ModoPagoProveedor,  on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.facturaEquipos.actualizar_estado()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.facturaEquipos.actualizar_estado()
        
        
    def __str__(self):
        return f'{self.facturaEquipos} - {self.abono} desde {self.fecha_pago}'
    
    
    
class Servicio(models.Model):
    nombre = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre
    
    
class FacturaServicios(models.Model):
    proveedor = models.ForeignKey(ProveedorEquipo,  on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio,  on_delete=models.CASCADE)
    mes_pago= models.DateField() #en el front que se pueda escoger solo el mes y año y aqui se guarda con el primero de ese mes
    fecha_emision= models.DateField()
    fecha_limite_pago= models.DateField(null=True, blank=True) 
    numeroFactura = models.CharField(max_length=300, null=True, blank=True, unique=True)  # SE GENERA AUTOMATICAMENTE
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    abono= models.DecimalField(max_digits=10, decimal_places=2, default=0) #SE PONE AUTOMATICAMEN
    pagado = models.BooleanField(default=False) #SE PONE AUTOMATICAMENTE
    
    modoCompra = models.ForeignKey(ModoCompra,  on_delete=models.CASCADE)

    presupuesto = models.ForeignKey(Presupuesto,  on_delete=models.CASCADE)
    digitador = models.ForeignKey(UserAccount,  on_delete=models.CASCADE)
    observacion = models.CharField(max_length=300, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.numeroFactura:  # Solo generar si el número de factura no existe
            last_invoice = FacturaServicios.objects.filter(servicio=self.servicio).order_by('id').last()
            if last_invoice:
                # Extraer el número de la última factura para ese servicio
                last_number = int(last_invoice.numeroFactura.split('-')[-1])
                new_number = last_number + 1
            else:
                new_number = 1  # Primera factura para este servicio
            self.numeroFactura = f"{self.servicio.nombre}-{new_number:03d}"
        super().save(*args, **kwargs)
    
    def actualizar_estado(self):
        self.pagado = self.abono >= self.valor
        self.save()
    def __str__(self):
        return f'{self.proveedor} - {self.fecha_emision} - {self.descripcion}'
    
    
class PagoFacturasServicios(models.Model):
    facturaServicios = models.ForeignKey(FacturaServicios, related_name='pagosServicios' ,on_delete=models.CASCADE)
    abono = models.DecimalField(max_digits=10, decimal_places=2)
    caja = models.ForeignKey(Caja,  on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    observacion = models.CharField(max_length=300, null=True, blank=True)
    modoPago = models.ForeignKey(ModoPagoProveedor,  on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.facturaServicios.actualizar_estado()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.facturaServicios.actualizar_estado()
        
        
    def __str__(self):
        return f'{self.facturaServicios} - {self.abono} - {self.fecha_pago}'
    
    
class VariosF(models.Model):
    nombre = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre
    
class FacturasVarios(models.Model):
    vario = models.ForeignKey(VariosF,  on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=300)
    fecha_emision= models.DateField()
    fecha_limite_pago= models.DateField(null=True, blank=True) 
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    abono= models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pagado = models.BooleanField(default=False)
    
    numeroFactura = models.CharField(max_length=300, null=True, blank=True)
    modoCompra = models.ForeignKey(ModoCompra,  on_delete=models.CASCADE)

    presupuesto = models.ForeignKey(Presupuesto,  on_delete=models.CASCADE)
    digitador = models.ForeignKey(UserAccount,  on_delete=models.CASCADE)
    observacion = models.CharField(max_length=300, null=True, blank=True)
    
    def actualizar_estado(self):
        self.pagado = self.abono >= self.valor
        self.save()
    def __str__(self):
        return f'{self.vario} - {self.fecha_emision} - {self.descripcion}'
    

class PagoFacturasVarios(models.Model):
    facturaVarios = models.ForeignKey(FacturasVarios, related_name='pagosVarios' ,on_delete=models.CASCADE)
    abono = models.DecimalField(max_digits=10, decimal_places=2)
    caja = models.ForeignKey(Caja,  on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    observacion = models.CharField(max_length=300, null=True, blank=True)
    modoPago = models.ForeignKey(ModoPagoProveedor,  on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.facturaVarios.actualizar_estado()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.facturaVarios.actualizar_estado()
        
        
    def __str__(self):
        return f'{self.facturaVarios} - {self.abono} - {self.fecha_pago}'
    
    
    
class Vehiculos(models.Model):
    nombre = models.CharField(max_length=300)
    anio = models.IntegerField()
    def __str__(self):
        return self.nombre
    
class InsumoVehiculo(models.Model):
    nombre = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre
    
class FacturasVehiculos(models.Model):
    vehiculo = models.ForeignKey(Vehiculos,  on_delete=models.CASCADE)
    insumoVehiculo = models.ForeignKey(InsumoVehiculo,  on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=300)
    kilometraje = models.DecimalField(max_digits=10, decimal_places=2)
    
    fecha_emision= models.DateField()
    fecha_limite_pago= models.DateField(null=True, blank=True) 
    
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    abono= models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pagado = models.BooleanField(default=False)
    
    modoCompra = models.ForeignKey(ModoCompra,  on_delete=models.CASCADE)

    presupuesto = models.ForeignKey(Presupuesto,  on_delete=models.CASCADE)
    digitador = models.ForeignKey(UserAccount,  on_delete=models.CASCADE)
    observacion = models.CharField(max_length=300, null=True, blank=True)
    
    def actualizar_estado(self):
        self.pagado = self.abono >= self.valor
        self.save()
    def __str__(self):
        return f'{self.vehiculo} - {self.fecha_emision} - {self.descripcion}'
    

    
class PagoFacturasVehiculos(models.Model):
    facturaVehiculos = models.ForeignKey(FacturasVehiculos, related_name='pagosVehiculos' ,on_delete=models.CASCADE)
    abono = models.DecimalField(max_digits=10, decimal_places=2)
    caja = models.ForeignKey(Caja,  on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    observacion = models.CharField(max_length=300, null=True, blank=True)
    modoPago = models.ForeignKey(ModoPagoProveedor,  on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.facturaVehiculos.actualizar_estado()
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.facturaVehiculos.actualizar_estado()
        
    def __str__(self):
        return f'{self.facturaVehiculos} - {self.abono} - {self.fecha_pago}'
    
    
#++++=============+++++++
class Colaboradores(models.Model):
    nombre = models.CharField(max_length=300)
    usuario = models.ForeignKey(UserAccount,  on_delete=models.CASCADE)
    valor_dia = models.DecimalField(max_digits=4, decimal_places=2)
    valor_comision_normal = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    valor_comision_cambio = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    def __str__(self):
        return self.nombre
    
class PlanillaColaboradores(models.Model):
    colaborador = models.ForeignKey(Colaboradores,  on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    
    dias_normales = models.DecimalField(max_digits=4, decimal_places=2)
    dias_extras = models.DecimalField(max_digits=4, decimal_places=2)
    dias_feriados = models.DecimalField(max_digits=4, decimal_places=2)
    
    valor_dias_normales = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    valor_dias_extras = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    valor_dias_feriados = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    
    valor_total =models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    abono =models.DecimalField(max_digits=5, decimal_places=2, default=0)
    pagado = models.BooleanField(default=False)
    
    observacion = models.CharField(max_length=300, null=True, blank=True)
    modoPago = models.ForeignKey(ModoPagoProveedor,  on_delete=models.CASCADE)
    presupuesto = models.ForeignKey(Presupuesto,  on_delete=models.CASCADE)
    observacion = models.CharField(max_length=300, null=True, blank=True)
    digitador = models.ForeignKey(UserAccount,  on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.colaborador} - {self.valor_total} '
    def save(self, *args, **kwargs):
        self.valor_dias_normales = self.dias_normales * self.colaborador.valor_dia
        self.valor_dias_extras = self.dias_extras * self.colaborador.valor_dia
        self.valor_dias_feriados = self.dias_feriados * self.colaborador.valor_dia
        self.valor_total = self.valor_dias_normales + self.valor_dias_extras + self.valor_dias_feriados
        super().save(*args, **kwargs)
    
    def actualizar_estado(self):
        self.pagado = self.abono >= self.valor_total
        self.save()

    
    
class PagoPlanillaColaboradores(models.Model):
    planillaColaboradores = models.ForeignKey(PlanillaColaboradores, related_name='pagosPlanilla' , on_delete=models.CASCADE)
    abono = models.DecimalField(max_digits=10, decimal_places=2)
    caja = models.ForeignKey(Caja,  on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    observacion = models.CharField(max_length=300, null=True, blank=True)
    modoPago = models.ForeignKey(ModoPagoProveedor,  on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.planillaColaboradores.actualizar_estado()
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.planillaColaboradores.actualizar_estado()
        
    def __str__(self):
        return f'{self.planillaColaboradores} - {self.abono} - {self.fecha_pago}'
    
    

class PlanillaComisiones(models.Model):
    colaborador = models.ForeignKey(Colaboradores,  on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    instalaciones_normales = models.DecimalField(max_digits=4, decimal_places=2)
    instalaciones_cambios = models.DecimalField(max_digits=4, decimal_places=2)
    valor_instalaciones_normales = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    valor_instalaciones_cambio = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    valor_total_comisiones =models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    abono =models.DecimalField(max_digits=5, decimal_places=2, default=0)
    pagado = models.BooleanField(default=False)
    
    observacion = models.CharField(max_length=300, null=True, blank=True)
    modoPago = models.ForeignKey(ModoPagoProveedor,  on_delete=models.CASCADE)
    presupuesto = models.ForeignKey(Presupuesto,  on_delete=models.CASCADE)
    observacion = models.CharField(max_length=300, null=True, blank=True)
    digitador = models.ForeignKey(UserAccount,  on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.colaborador} - {self.valor_total_comisiones} '
    def save(self, *args, **kwargs):
        self.valor_instalaciones_normales = self.instalaciones_normales * self.colaborador.valor_comision_normal
        self.valor_instalaciones_cambio = self.instalaciones_cambios * self.colaborador.valor_comision_cambio

        self.valor_total_comisiones = self.valor_instalaciones_normales + self.valor_instalaciones_cambio
        super().save(*args, **kwargs)
    
    def actualizar_estado(self):
        self.pagado = self.abono >= self.valor_total_comisiones
        self.save()

class PagoPlanillaComisiones(models.Model):
    planillaComisiones = models.ForeignKey(PlanillaComisiones, related_name='pagosPlanillaComisiones' , on_delete=models.CASCADE)
    abono = models.DecimalField(max_digits=10, decimal_places=2)
    caja = models.ForeignKey(Caja,  on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    observacion = models.CharField(max_length=300, null=True, blank=True)
    modoPago = models.ForeignKey(ModoPagoProveedor,  on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.planillaComisiones.actualizar_estado()
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.planillaComisiones.actualizar_estado()
        
    def __str__(self):
        return f'{self.planillaComisiones} - {self.abono} - {self.fecha_pago}'
    