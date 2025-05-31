from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer, RegistroSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cursos.models import Inscripcion, Curso

class RegistroView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RegistroSerializer
    permission_classes = [AllowAny]

class ListaUsuariosView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard') 
    
class RegistroViewTemplate(CreateView):
    template_name = 'usuarios/register.html'
    form_class = RegistroForm
    success_url = reverse_lazy('login')

@login_required
def dashboard(request):
    usuario = request.user
    inscripciones = Inscripcion.objects.filter(usuario=usuario).select_related('curso')
    cursos = [ins.curso for ins in inscripciones]

    context = {
        'cursos': cursos
    }
    return render(request, 'usuarios/dashboard.html', context)

def inicio(request):
    return render(request, 'usuarios/inicio.html')