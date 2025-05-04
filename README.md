# StudyHub
 Education and Programming in this place

# Accest to admin
 Ejecutar en la consola de visual el comando
 'python manga.py runserver'

 En el navegador ingresar el siguiqnete link:
 'http://localhost:8000/admin/'

 Ingresar las credenciales

 username: AlejoZT697

 password: 250423

# Acceso a usuarios API

http://127.0.0.1:8000/api/usuarios/registro/
http://127.0.0.1:8000/api/token/
http://127.0.0.1:8000/api/usuarios/lista/

Falta terminal el crud para ver la lista de usuarios y se puedan realizar todos los metodos

GET, POST, HEAD, OPTIONS

# Acceso a cursos API

http://127.0.0.1:8000/api/cursos/cursos/

# Notas

Se pueden agregar cursos y usuarios directamente desde el panel de administrador

# Steven 
Revise los cambios hechos dentro del admin ya se pueden matricular ciertos usuarios en algún curso 

# Endpoints

# Autentiación(Simple JWT)
| Acción        | Endpoint          | Método |
| ------------- | ----------------- | ------ |
| Obtener token | `/token/`         | POST   |
| Refresh token | `/token/refresh/` | POST   |

# Cursos
| Acción                     | Endpoint        | Método |
| -------------------------- | --------------- | ------ |
| Listar cursos              | `/cursos/`      | GET    |
| Detalle de curso           | `/cursos/<id>/` | GET    |
| Crear curso (si permitido) | `/cursos/`      | POST   |

# Inscripción
| Acción               | Endpoint          | Método |
| -------------------- | ----------------- | ------ |
| Listar inscripciones | `/inscripciones/` | GET    |
| Inscribir estudiante | `/inscripciones/` | POST   |

# Lecciones
| Acción                  | Endpoint                     | Método   |
| ----------------------- | ---------------------------- | -------- |
| Listar lecciones        | `/lecciones/`                | GET      |
| Ver lecciones por curso | (custom si aplicaste filtro) |          |
| Crear/editar lección    | `/lecciones/`                | POST/PUT |

# Progreso
| Acción                       | Endpoint                | Método |
| ---------------------------- | ----------------------- | ------ |
| Ver progreso del usuario     | `/progreso/`            | GET    |
| Registrar lección completada | `/progreso/`            | POST   |
| Ver avance en un curso       | `/progreso/curso/<id>/` | GET    |

# Quizzes
| Acción                 | Endpoint         | Método |
| ---------------------- | ---------------- | ------ |
| Listar quizzes         | `/quizzes/`      | GET    |
| Ver preguntas del quiz | `/quizzes/<id>/` | GET    |

# Respuestas Quizzes
| Acción                     | Endpoint       | Método |
| -------------------------- | -------------- | ------ |
| Enviar respuesta           | `/respuestas/` | POST   |
| Ver respuestas del usuario | `/respuestas/` | GET    |

# Puntaje en quiz
| Acción              | Endpoint                 | Método |
| ------------------- | ------------------------ | ------ |
| Ver puntaje en quiz | `/quizzes/<id>/puntaje/` | GET    |

# Certficados
| Acción                         | Endpoint                           | Método |
| ------------------------------ | ---------------------------------- | ------ |
| Emitir certificado (si cumple) | `/certificados/emitir/<curso_id>/` | POST   |


