from django.urls import path
from .views import RegistroView, ListaUsuariosView, CustomLoginView, RegistroViewTemplate, dashboard, inicio
from rest_framework import routers
from django.contrib.auth.views import LogoutView

router = routers.DefaultRouter()
router.register(r'registro', RegistroView, 'registro')
router.register(r'lista', ListaUsuariosView, 'lista')

urlpatterns = [
    path('', inicio, name='inicio'),
    path('registroapi/', RegistroView.as_view(), name='registro'),
    path('lista/', ListaUsuariosView.as_view(), name='lista_usuarios'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('registro/', RegistroViewTemplate.as_view(), name='register'),
    path('dashboard/', dashboard, name='dashboard'),
]