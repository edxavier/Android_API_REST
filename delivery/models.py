from django.db import models
from geoposition.fields import GeopositionField


# Create your models here.


class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=11)
    coordenadas = GeopositionField()

    def __unicode__(self):
        return self.nombre

#------------------------------------------------------------------------
class Menu(models.Model):
    nombre = models.CharField(unique=True, max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='menu')

    def __unicode__(self):
        return self.nombre

    def precio_combo(self):
        return "C$" + self.precio.__str__()

    def vista_previa(self):
        return """
                <img src="%s" height="100" width="100">
            """ % self.imagen.url

    vista_previa.allow_tags = True
    vista_previa.admin_order_field = 'imagen'
    precio_combo.admin_order_field = 'precio'

#------------------------------------------------------------------------
class Cliente(models.Model):
    social_id = models.CharField(max_length=100, unique=True)
    img_url = models.CharField(max_length=200,default="")
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

#------------------------------------------------------------------------
class Pedido(models.Model):
    TIPO_ESTADO = (
        ('EN ESPERA', 'EN ESPERA'),
        ('ATENDIENDOSE', 'ATENDIENDOSE'),
        ('EN CAMINO', 'EN CAMINO'),
        ('CANCELADO', 'CANCELADO'),
        ('RECHAZADO', 'RECHAZADO'),
    )
    cliente = models.CharField(max_length=100)
    social_id = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    estado = models.CharField(choices=TIPO_ESTADO, max_length=30, )

    def __unicode__(self):
        return " orden:" + str(self.id)


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido)
    menu = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    total = models.FloatField()

#------------------------------------------------------------------------
class Comentario(models.Model):
    cliente = models.CharField(max_length=100)
    imagen_url = models.CharField(max_length=100)
    comentario = models.CharField(max_length=400)
    def __unicode__(self):
        return self.cliente