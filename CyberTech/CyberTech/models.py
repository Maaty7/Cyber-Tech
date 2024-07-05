from django.db import models

# Create your models here.

class Tecnologia(models.Model):
    id_producto = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50, null=False, blank=False)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    nombreImagen = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return (
            str(self.nombre)
            + ", precio: "
            + str(self.precio)
        )


class Hardware(models.Model):
    id_producto = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50, null=False, blank=False)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    nombreImagen = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return (
            str(self.nombre)
            + ", precio: "
            + str(self.precio)
        )

class Periferico(models.Model):
    id_producto = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50, null=False, blank=False)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    nombreImagen = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return (
            str(self.nombre)
            + ", precio: "
            + str(self.precio)
        )

class Electrodomestico(models.Model):
    id_producto = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50, null=False, blank=False)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    nombreImagen = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return (
            str(self.nombre)
            + ", precio: "
            + str(self.precio)
        )


    