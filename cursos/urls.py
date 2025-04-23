from django.urls import path,include
from rest_framework import routers
from .views import CursoView, InscripcionCursoView, LeccionView

router = routers.DefaultRouter()
router.register(r'lecciones', LeccionView)

urlpatterns = [
    path('cursos/', CursoView.as_view(), name = "cursos"),
    path('<int:curso_id>/inscribirse/', InscripcionCursoView.as_view(), name='inscribirse-curso'),
] + router.urls