from rest_framework import serializers
from .models import Curso, Inscripcion, Leccion, Progreso, Quiz, Pregunta, Opcion, Respuesta

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

class ProgresoSerializer(serializers.Serializer):

    class Meta:
        model = Progreso
        fields = '__all__'

class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = ['id', 'texto']

class PreguntaSerializer(serializers.ModelSerializer):
    opciones = OpcionSerializer(many = True, read_only = True)

    class Meta:
        model = Pregunta
        fields = ['id', 'texto', 'opciones']

class QuizSerializer(serializers.ModelSerializer):
    preguntas = PreguntaSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'titulo', 'descripcion', 'preguntas']

class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = '__all__'
        read_only_fields = ['usuario']