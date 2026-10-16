from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_estreno = models.DateField()
    director = models.CharField(max_length=100)
    calificacion = models.DecimalField(max_digits=3, decimal_places=1, help_text="Ejemplo: 8.5")

    def __str__(self):
        return self.titulo

class Serie(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_estreno = models.DateField()
    temporadas = models.IntegerField()
    finalizada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo