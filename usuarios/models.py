from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    ROL_CHOICES = (
        ('estudiante', 'Estudiante'),
        ('instructor', 'Instructor'),
        ('admin', 'Administrador'),
    )
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='estudiante')

    def __str__(self):
        return f"{self.username} ({self.rol})"
    #A