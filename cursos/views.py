from rest_framework import generics, permissions, viewsets
from .models import Curso, Inscripcion
from .serializers import CursoSerializer, InscripcionSerializer

# Create your views here.

class CursoView(viewsets.ViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [permissions.AllowAny]

class InscripcionCursoView(generics.ListAPIView):
    serializer_class = InscripcionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        curso_id = self.kwargs.get('curso_id')
        serializer.save(usuario = self.request.user, curso_id = curso_id)