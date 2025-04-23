from rest_framework import serializers
from .models import Curso, Inscripcion, Leccion

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        field = '__all__'
        readr_only_fields = ['usuario']

class LeccionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Leccion
        fields = '__all__'