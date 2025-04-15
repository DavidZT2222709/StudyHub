from django.urls import path
from .views import RegistroView, ListaUsuariosView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'registro', RegistroView, 'registro')
router.register(r'lista', ListaUsuariosView, 'lista')

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),
    path('lista/', ListaUsuariosView.as_view(), name='lista_usuarios'),
]
