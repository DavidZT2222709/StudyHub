from django.contrib import admin
from .models import Curso, Inscripcion, Leccion

# Register your models here.

class InscripcionAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'curso', 'fecha_inscripcion']
    search_fields = ['usuario__username', 'curso__titulo']

class LeccionInline(admin.TabularInline):
    model = Leccion
    extra = 1

class CursoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = [LeccionInline]

admin.site.register(Curso, CursoAdmin)
admin.site.register(Inscripcion, InscripcionAdmin)

@admin.register(Leccion)
class LeccionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'curso', 'orden')
    list_filter = ('curso',)
    search_fields = ('titulo', 'curso_titulo')
    ordering = ('curso', 'orden')