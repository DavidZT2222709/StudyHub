from rest_framework import routers
from django.urls import path, include
from cursos import views

router = routers.DefaultRouter()
router.register(r'cursos', views.CursoView, 'cursos')

urlpatterns = [
    path('cursos/', include(router.urls))
]
