from django.db import models

# Create your models here.
class Producto(models.Model):
    id= models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    talla = models.CharField(max_length=50)
    valor = models.IntegerField()

    def __str__(self):
        return self.nombre