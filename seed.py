import os
import django
import random
from faker import Faker
from django.utils import timezone

# Inicializa Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # cambia si tu proyecto se llama distinto
django.setup()

from cursos.models import Curso, Leccion, Progreso, Inscripcion, Quiz, Pregunta, Opcion, Respuesta
from usuarios.models import Usuario  # o get_user_model() si prefieres

fake = Faker()

# Crear usuarios estudiantes
print("Creando usuarios...")
usuarios = []
for i in range(10):
    user = Usuario.objects.create_user(
        username=fake.unique.user_name(),
        email=fake.unique.email(),
        password="test1234",
        rol='estudiante'
    )
    usuarios.append(user)

# Crear cursos
print("Creando cursos...")
cursos = []
for i in range(3):
    curso = Curso.objects.create(
        title=f"Curso de {fake.word().capitalize()}",
        description=fake.paragraph(nb_sentences=3),
        time=random.randint(1, 10)
    )
    cursos.append(curso)

# Crear lecciones por curso
print("Creando lecciones...")
lecciones = []
for curso in cursos:
    for i in range(random.randint(4, 7)):
        leccion = Leccion.objects.create(
            curso=curso,
            titulo=fake.sentence(nb_words=5),
            descripcion=fake.paragraph(),
            contenido_texto=fake.text(max_nb_chars=300),
            video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ" if random.choice([True, False]) else None,
            orden=i + 1
        )
        lecciones.append(leccion)

# Inscribir usuarios aleatoriamente
print("Inscribiendo usuarios...")
for usuario in usuarios:
    cursos_inscritos = random.sample(cursos, k=random.randint(1, len(cursos)))
    for curso in cursos_inscritos:
        Inscripcion.objects.get_or_create(usuario=usuario, curso=curso)

# Crear progreso aleatorio
print("Creando progreso...")
for usuario in usuarios:
    cursos_usuario = Curso.objects.filter(inscripciones__usuario=usuario)
    for curso in cursos_usuario:
        lecciones_curso = Leccion.objects.filter(curso=curso)
        completadas = random.sample(list(lecciones_curso), k=random.randint(0, len(lecciones_curso)))
        for leccion in completadas:
            Progreso.objects.get_or_create(
                usuario=usuario,
                leccion=leccion,
                defaults={'completado': True, 'fecha': timezone.now()}
            )

print("Creando quizzes y preguntas...")

for curso in cursos:
    quiz = Quiz.objects.create(
        curso=curso,
        titulo=f"Quiz Final - {curso.title}",
        descripcion="Evaluación del curso",
        publicado=True
    )
    for i in range(5):  # 5 preguntas
        pregunta = Pregunta.objects.create(
            quiz=quiz,
            texto=fake.sentence(nb_words=6)
        )
        correct_index = random.randint(0, 3)
        for j in range(4):  # 4 opciones
            Opcion.objects.create(
                pregunta=pregunta,
                texto=fake.sentence(nb_words=3),
                es_correcta=(j == correct_index)
            )

print("Simulando respuestas de estudiantes...")

for usuario in usuarios:
    for quiz in Quiz.objects.all():
        preguntas = quiz.preguntas.all()
        for pregunta in preguntas:
            opciones = pregunta.opciones.all()
            seleccion = random.choice(opciones)
            Respuesta.objects.get_or_create(
                usuario=usuario,
                pregunta=pregunta,
                opcion=seleccion
            )

print("Quizzes, preguntas y respuestas simuladas exitosamente.")

print("Datos de prueba generados correctamente.")