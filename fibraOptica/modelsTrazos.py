from django.db import models
from accounts.models import UserAccount
from .modelsCuartoEquipos import TrazoPachcordNA

from .modelsCajasMufas import MufaNA, CajaNapNA
from .modelsFibras import HiloNA



class Trazo1NA(models.Model): # es por donde pasa o es todo
    sal_trazoPatchcord = models.ForeignKey(TrazoPachcordNA,related_name='trazo1', on_delete=models.CASCADE)
    
    lleg_Mufa = models.ForeignKey(MufaNA, on_delete=models.CASCADE, null=True, blank=True)
    lleg_Caja = models.ForeignKey(CajaNapNA, on_delete=models.CASCADE, null=True, blank=True)
    
    hiloTrazado =models.ForeignKey(HiloNA,related_name='hiloTrazado1', on_delete=models.CASCADE, null=True, blank=True)
    hiloSalida =models.ForeignKey(HiloNA,related_name='hiloSalida1', on_delete=models.CASCADE, null=True, blank=True)
    
    tipoConexion = models.IntegerField(choices=[(1, 'continua mismo hilo sin fusion'),(2, 'fusion a spliter'), (3, 'Fusion con otro hilo de la misma fibra'), (4, 'Fusion con otro hilo de otra fibra'), (5, 'Hilo suelto')], default=1)
    
    comentario = models.CharField(max_length=300,null=True, blank=True )
    fecha_instalacion = models.DateField( null=True, blank=True )
    verificado = models.IntegerField(choices=[(1, 'No'), (2, 'Si')], default=1)
    
    def __str__(self):
        return f'{self.sal_trazoPatchcord} - {self.lleg_Mufa} - lleg:{self.lleg_Caja}'
    
    

class Trazo2NA(models.Model):
    sal_trazo1 = models.ForeignKey(Trazo1NA,related_name='trazo2', on_delete=models.CASCADE)
    
    lleg_Mufa = models.ForeignKey(MufaNA, on_delete=models.CASCADE, null=True, blank=True)
    lleg_Caja = models.ForeignKey(CajaNapNA, on_delete=models.CASCADE, null=True, blank=True)
    
    hiloTrazado =models.ForeignKey(HiloNA,related_name='hiloTrazado2', on_delete=models.CASCADE, null=True, blank=True)
    hiloSalida =models.ForeignKey(HiloNA,related_name='hiloSalida2', on_delete=models.CASCADE, null=True, blank=True)
    
    tipoConexion = models.IntegerField(choices=[(1, 'continua mismo hilo sin fusion'),(2, 'fusion a spliter'), (3, 'Fusion con otro hilo de la misma fibra'), (4, 'Fusion con otro hilo de otra fibra'), (5, 'Hilo suelto')], default=1)
    
    comentario = models.CharField(max_length=300,null=True, blank=True )
    fecha_instalacion = models.DateField( null=True, blank=True )
    verificado = models.IntegerField(choices=[(1, 'No'), (2, 'Si')], default=1)
    
    def __str__(self):
        return f'sal:{self.sal_trazo1} - lleg:{self.lleg_Mufa} - lleg:{self.lleg_Caja}'

class Trazo3NA(models.Model):
    sal_trazo2 = models.ForeignKey(Trazo2NA,related_name='trazo3', on_delete=models.CASCADE)
    
    lleg_Mufa = models.ForeignKey(MufaNA, on_delete=models.CASCADE, null=True, blank=True)
    lleg_Caja = models.ForeignKey(CajaNapNA, on_delete=models.CASCADE, null=True, blank=True)
    
    hiloTrazado =models.ForeignKey(HiloNA,related_name='hiloTrazado3', on_delete=models.CASCADE, null=True, blank=True)
    hiloSalida =models.ForeignKey(HiloNA,related_name='hiloSalida3', on_delete=models.CASCADE, null=True, blank=True)
    
    tipoConexion = models.IntegerField(choices=[(1, 'continua mismo hilo sin fusion'),(2, 'fusion a spliter'), (3, 'Fusion con otro hilo de la misma fibra'), (4, 'Fusion con otro hilo de otra fibra'), (5, 'Hilo suelto')], default=1)
    
    comentario = models.CharField(max_length=300,null=True, blank=True )
    fecha_instalacion = models.DateField( null=True, blank=True )
    verificado = models.IntegerField(choices=[(1, 'No'), (2, 'Si')], default=1)
    
    def __str__(self):
        return f'sal:{self.sal_trazo2} - lleg:{self.lleg_Mufa} - lleg:{self.lleg_Caja}'
    
    
class Trazo4NA(models.Model):
    sal_trazo3 = models.ForeignKey(Trazo3NA, on_delete=models.CASCADE)
    
    lleg_Mufa = models.ForeignKey(MufaNA, on_delete=models.CASCADE, null=True, blank=True)
    lleg_Caja = models.ForeignKey(CajaNapNA, on_delete=models.CASCADE, null=True, blank=True)
    
    hiloTrazado =models.ForeignKey(HiloNA,related_name='hiloTrazado4', on_delete=models.CASCADE, null=True, blank=True)
    hiloSalida =models.ForeignKey(HiloNA,related_name='hiloSalida4', on_delete=models.CASCADE, null=True, blank=True)
    
    tipoConexion = models.IntegerField(choices=[(1, 'continua mismo hilo sin fusion'),(2, 'fusion a spliter'), (3, 'Fusion con otro hilo de la misma fibra'), (4, 'Fusion con otro hilo de otra fibra'), (5, 'Hilo suelto')], default=1)
    
    comentario = models.CharField(max_length=300,null=True, blank=True )
    fecha_instalacion = models.DateField( null=True, blank=True )
    verificado = models.IntegerField(choices=[(1, 'No'), (2, 'Si')], default=1)
    
    
    
class Trazo5NA(models.Model):
    sal_trazo4 = models.ForeignKey(Trazo4NA, on_delete=models.CASCADE)
    
    lleg_Mufa = models.ForeignKey(MufaNA, on_delete=models.CASCADE, null=True, blank=True)
    lleg_Caja = models.ForeignKey(CajaNapNA, on_delete=models.CASCADE, null=True, blank=True)
    
    hiloTrazado =models.ForeignKey(HiloNA,related_name='hiloTrazado5', on_delete=models.CASCADE, null=True, blank=True)
    hiloSalida =models.ForeignKey(HiloNA,related_name='hiloSalida5', on_delete=models.CASCADE, null=True, blank=True)
    
    tipoConexion = models.IntegerField(choices=[(1, 'continua mismo hilo sin fusion'),(2, 'fusion a spliter'), (3, 'Fusion con otro hilo de la misma fibra'), (4, 'Fusion con otro hilo de otra fibra'), (5, 'Hilo suelto')], default=1)
    
    comentario = models.CharField(max_length=300,null=True, blank=True )
    fecha_instalacion = models.DateField( null=True, blank=True )
    verificado = models.IntegerField(choices=[(1, 'No'), (2, 'Si')], default=1)
    
