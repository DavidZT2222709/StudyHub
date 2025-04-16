from django.contrib import admin
from .models import Curso, Inscripcion

# Register your models here.

class InscripcionAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'curso', 'fecha_inscripcion']
    search_fields = ['usuario__username', 'curso__titulo']

admin.site.register(Curso)
admin.site.register(Inscripcion, InscripcionAdmin)