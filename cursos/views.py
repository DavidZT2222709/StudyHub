from rest_framework import generics, permissions, viewsets, decorators, response, exceptions
from .models import Curso, Inscripcion, Leccion, Progreso, Quiz, Respuesta, Certificado
from .serializers import CursoSerializer, InscripcionSerializer, LeccionSerializer, ProgresoSerializer, QuizSerializer, RespuestaSerializer

# Create your views here.

class CursoView(viewsets.ModelViewSet):
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

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAuthenticated])

def emitir_certificado(request, curso_id):
    usuario = request.user

    total_lecciones = Leccion.objects.filter(curso_id=curso_id).count()
    completadas = Progreso.objects.filter(
        usuario=usuario, leccion__curso_id=curso_id, completado=True
    ).count()

    if total_lecciones == 0 or completadas < total_lecciones:
        return response.Response({"detalle": "Aún no has completado todas las lecciones."}, status=400)

    quizzes = Quiz.objects.filter(curso_id=curso_id)
    respuestas = Respuesta.objects.filter(usuario=usuario, pregunta__quiz__in=quizzes)

    total_preguntas = respuestas.count()
    correctas = respuestas.filter(opcion__es_correcta=True).count()
    puntaje = round((correctas / total_preguntas) * 100, 2) if total_preguntas else 0

    if puntaje < 70:
        return response.Response({"detalle": f"Tu puntaje es {puntaje}%. Debes obtener al menos 70%."}, status=400)

    # Generar certificado (solo una vez)
    certificado, creado = Certificado.objects.get_or_create(
        usuario=usuario,
        curso_id=curso_id,
        defaults={"puntaje_final": puntaje, "generado": True}
    )

    if not creado:
        return response.Response({"detalle": "Ya tienes un certificado para este curso."}, status=200)

    return response.Response({
        "mensaje": "🎉 Felicitaciones, terminaste el curso, aqui puedes descargar tu certificado",
        "curso": certificado.curso.titulo,
        "puntaje": certificado.puntaje_final,
        "fecha": certificado.fecha_emision
    })