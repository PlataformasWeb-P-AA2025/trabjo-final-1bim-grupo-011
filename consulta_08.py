# Obtener el usuario con más publicaciones.
from sqlalchemy.orm import Session
from genera_tablas import engine, Usuario

# Crear una sesión
session = Session(engine)

print("\nUsuario con más publicaciones:")

# Obtener todos los usuarios como objetos
usuarios = session.query(Usuario).all()

# Buscar el usuario con más publicaciones
usuario_mas_publicaciones = None
max_publicaciones = -1

for usuario in usuarios:
    num_publicaciones = len(usuario.publicaciones)
    if num_publicaciones > max_publicaciones:
        max_publicaciones = num_publicaciones
        usuario_mas_publicaciones = usuario

if usuario_mas_publicaciones:
    print(f"- {usuario_mas_publicaciones.nombre} ({max_publicaciones} publicaciones)")

session.close()