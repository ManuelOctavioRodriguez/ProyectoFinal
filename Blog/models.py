from django.db import models
from Perfiles.models import Perfil

class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='articulos/', null=True, blank=True)

    def __str__(self):
        return self.titulo