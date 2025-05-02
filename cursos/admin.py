from django import forms
from django.contrib import admin
from .models import Curso, Inscripcion, Leccion, Progreso, Quiz, Pregunta, Opcion, Respuesta, Certificado

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

class ProgresoAdminForm(forms.ModelForm):
    class Meta:
        model = Progreso
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        usuario = cleaned_data.get("usuario")
        leccion = cleaned_data.get("leccion")

        if usuario and leccion:
            curso = leccion.curso
            if not Inscripcion.objects.filter(usuario=usuario, curso=curso).exists():
                raise forms.ValidationError("Este usuario no está inscrito en el curso de esta lección.")

        return cleaned_data

class ProgresoAdmin(admin.ModelAdmin):
    form = ProgresoAdminForm
    list_display = ('usuario', 'leccion', 'completado', 'fecha')

admin.site.register(Progreso, ProgresoAdmin)

class OpcionInline(admin.TabularInline):
    model = Opcion
    extra = 2

class PreguntaInline(admin.StackedInline):
    model = Pregunta
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    inlines = [PreguntaInline]

class PreguntaAdmin(admin.ModelAdmin):
    inlines = [OpcionInline]

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta)

class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'curso', 'puntaje_final', 'fecha_emision')
    list_filter = ('curso',)
    search_fields = ('usuario__username', 'curso__titulo')

admin.site.register(Certificado, CertificadoAdmin)