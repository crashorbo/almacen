import uuid

from django.db import models
from django.utils import timezone

from user.models import User

# Create your models here.
class Unidad(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    nombre_completo = models.CharField(max_length=100)
    nombre_corto = models.CharField(max_length=10)
    deleted = models.BooleanField(default=False)
    
    created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True)
    
    def __str__(self):
        return f'{self.nombre_completo} - {self.nombre_corto}'
    
    
class Categoria(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True,
                                   null=True)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True)
    

class Articulo(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=300)
    unidad = models.ForeignKey(Unidad,
                               on_delete=models.CASCADE)
    numero_parte = models.CharField(max_length=50)
    deleted = models.BooleanField(default=False)
    
    created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True)
    
    
class Almacen(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True,
                                   null=True)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True)
    
class AlmacenArticulo(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    categoria =models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,
                             related_name='user',
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True)
    updated = models.DateTimeField(blank=True, null=True)
    user_updated = models.ForeignKey(User,
                                     related_name='user_updated',
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True)