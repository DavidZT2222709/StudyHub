from django.db import models
from django.conf import settings
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
    

class Progreso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    leccion = models.ForeignKey('Leccion', on_delete=models.CASCADE)
    completado = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario','leccion')

    def __str__(self):
        return f"{self.usuario.username} - {self.leccion.titulo} - {'✔️' if self.completado else '❌'}"
    
class Quiz(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='quizzes')
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titulo} ({self.curso.title})"
    
class Pregunta(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='preguntas')
    texto = models.TextField()

    def __str__(self):
        return f"Pregunta: {self.texto}"
    
class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='opciones')
    texto = models.CharField(max_length=255)
    es_correcta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto
    
class Respuesta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE)
    respondido_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'pregunta')

class Certificado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    puntaje_final = models.FloatField()
    generado = models.BooleanField(default=False)

    class Meta:
        unique_together = ('usuario', 'curso')

    def __str__(self):
        return f"Certificado - {self.usuario.username} - {self.curso.title}"