from django.db import models

# Create your models here.
class Servicio(models.Model):
    idCategoria = models.CharField(primary_key=True,max_length=20,verbose_name='idCategoria',default='')
    nombreServicio = models.CharField(max_length=50,verbose_name='nombreServicio',default='')
    def _str_(self):
        return self.nombreServicio

class Proveedor(models.Model):
    
    rut = models.CharField(primary_key=True,max_length=50,verbose_name='rut',default='')
    nombreProveedor = models.CharField(max_length=50,verbose_name='nombreProveedor',default='')
    descripcion = models.CharField(max_length=500,verbose_name='descripcion',default='')
    telefono = models.CharField(max_length=50,verbose_name='telefono',default='')
    emailProveedor = models.CharField(max_length=50,verbose_name='emailProveedor',default='')
    tipoServicio = models.ForeignKey(Servicio,on_delete=models.CASCADE)
    def _str_(self):
        return self.rut


