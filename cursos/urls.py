from django.urls import path,include
from rest_framework import routers
from .views import CursoView, InscripcionCursoView


urlpatterns = [
    path('cursos/', CursoView.as_view(), name = "cursos"),
   path('<int:curso_id>/inscribirse/', InscripcionCursoView.as_view(), name='inscribirse-curso'),
]