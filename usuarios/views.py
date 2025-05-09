from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer, RegistroSerializer
from rest_framework.permissions import AllowAny

class RegistroView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RegistroSerializer
    permission_classes = [AllowAny]

class ListaUsuariosView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

#A