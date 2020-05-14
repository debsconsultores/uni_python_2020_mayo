from django.db import models

from home.models import ClaseModelo


class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return "{}-{}".format(self.id,self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria,self).save()

    class Meta:
        verbose_name_plural="Categorias"
    

class SubCategoria(models.Model):
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    def __str__(self):
        return "{}-->{}".format(self.categoria,self.descripcion)

    class Meta:
        verbose_name_plural = "Sub Categorías"


class Marca(models.Model):
    descripcion = models.CharField(
        max_length=20,
        unique=True,
        null=False,
        blank=False
        )
    
    def __str__(self):
        return "{}".format(self.descripcion)
    
    class Meta:
        verbose_name_plural = "Marcas"


class Producto(models.Model):
    marca = models.ForeignKey(
        Marca,
        on_delete=models.DO_NOTHING
        )
    subcategoria = models.ForeignKey(
        SubCategoria,
        on_delete=models.CASCADE
        )
    descripcion = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False
        )
    precio = models.FloatField(default=0)
    
    cantidad = models.IntegerField(default=0)
    