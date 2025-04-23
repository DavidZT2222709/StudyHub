from django.db import models
from usuarios.models import Usuario


# Create your models here.

class Curso(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    time = models.IntegerField(help_text="Time in hours")

    def  __str__(self):
        return self.title
    
class Inscripcion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='inscripciones')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscripciones')
    fecha_inscripcion= models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['usuario', 'curso']

    def __str__(self):
        return f"{self.usuario.username} -> {self.curso.title}"
    
class Leccion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='lecciones')
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    contenido_texto = models.TextField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    pdf = models.FileField(upload_to='lecciones/pdfs/', blank=True, null=True)
    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.orden} - {self.titulo}"