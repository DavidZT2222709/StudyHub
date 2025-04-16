from django.urls import path,include
from rest_framework import routers
from .views import CursoView, InscripcionCursoView

router = routers.DefaultRouter()
router.register(r'cursos', CursoView, 'cursos')

urlpatterns = [
    path('cursos/', include(router.urls)),
   path('<int:curso_id>/inscribirse/', InscripcionCursoView.as_view(), name='inscribirse-curso'),
]