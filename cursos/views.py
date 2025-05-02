from rest_framework import generics, permissions, viewsets, decorators, response, exceptions
from .models import Curso, Inscripcion, Leccion, Progreso, Quiz, Respuesta
from .serializers import CursoSerializer, InscripcionSerializer, LeccionSerializer, ProgresoSerializer, QuizSerializer, RespuestaSerializer

# Create your views here.

class CursoView(generics.ListAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [permissions.AllowAny]

class InscripcionCursoView(generics.ListAPIView):
    serializer_class = InscripcionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        curso_id = self.kwargs.get('curso_id')
        serializer.save(usuario = self.request.user, curso_id = curso_id)

class LeccionView(viewsets.ModelViewSet):
    queryset = Leccion.objects.all()
    serializer_class = LeccionSerializer

class ProgresoView(viewsets.ModelViewSet):
    queryset = Progreso.objects.all()
    serializer_class = ProgresoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        usuario = self.request.user
        leccion = serializer.validated_data['leccion']
        curso = leccion.curso

        if not Inscripcion.objects.filter(usuario=usuario, curso=curso).exists():
            raise exceptions.ValidationError("No estás inscrito en el curso de esta lección.")

        serializer.save(usuario = self.request.user)

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])

def progreso_curso(request, curso_id):
    usuario = request.user
    total_lecciones = Leccion.objects.filter(curso_id=curso_id).count
    completadas = Progreso.objects.filter(
        usuario=usuario,
        leccion_curso_id = curso_id,
        completado = True
    ).count

    if total_lecciones == 0:
        porcentaje = 0
    else:
        porcentaje = (completadas / total_lecciones)*100

    return response.Response({
        "curso_id": curso_id,
        "usuario": usuario.username,
        "lecciones_totales": total_lecciones,
        "lecciones_completadas": completadas,
        "porcentaje": round(porcentaje, 2)
    })

class QuizViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quiz.objects.filter(publicado=True)
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticated]


class RespuestaViewSet(viewsets.ModelViewSet):
    serializer_class = RespuestaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Respuesta.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])

def calcular_puntaje(request, quiz_id):
    usuario = request.user

    # Obtener todas las respuestas del usuario para preguntas de ese quiz
    respuestas_usuario = Respuesta.objects.filter(
        usuario=usuario,
        pregunta__quiz_id=quiz_id
    ).select_related('opcion')

    total_preguntas = respuestas_usuario.count()
    correctas = respuestas_usuario.filter(opcion__es_correcta=True).count()

    puntaje = round((correctas / total_preguntas) * 100, 2) if total_preguntas else 0

    return response.Response({
        "usuario": usuario.username,
        "quiz_id": quiz_id,
        "total_preguntas_respondidas": total_preguntas,
        "respuestas_correctas": correctas,
        "puntaje": puntaje
    })