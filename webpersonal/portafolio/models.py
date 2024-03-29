"""Este módulo define los modelos de la aplicación portafolio."""

from django.db import models

class Project(models.Model):
    """Representa un proyecto dentro del portafolio."""
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        """Información de metadatos para el modelo Project."""
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        """Devuelve la representación en cadena del modelo."""
        return str(self.title)
