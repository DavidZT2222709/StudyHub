from django.urls import path
from rest_framework import routers
from .views import CursoView, InscripcionCursoView, LeccionView, ProgresoView, progreso_curso, QuizViewSet, RespuestaViewSet, calcular_puntaje, emitir_certificado

router = routers.DefaultRouter()
router.register(r'cursos', CursoView)
router.register(r'lecciones', LeccionView)
router.register(r'progreso', ProgresoView)
router.register(r'quizzes', QuizViewSet)
router.register(r'respuestas', RespuestaViewSet, basename='respuesta')

urlpatterns = [
    path('<int:curso_id>/inscribirse/', InscripcionCursoView.as_view(), name='inscribirse-curso'),
    path('progreso/curso/<int:curso_id>/', progreso_curso, name='progreso-curso'),
    path('quizzes/<int:quiz_id>/puntaje/', calcular_puntaje, name='puntaje-quiz'),
    path('certificados/emitir/<int:curso_id>/', emitir_certificado, name='emitir-certificado'),
] + router.urls