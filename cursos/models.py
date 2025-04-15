from django.db import models

# Create your models here.

class Curso(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    time = models.IntegerField(help_text="Time in hours")

    def  __str__(self):
        return self.title
    