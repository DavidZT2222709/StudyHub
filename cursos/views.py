from rest_framework import viewsets
from .models import Curso
from .serializers import CursoSerializer

# Create your views here.

class CursoView(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer