#Mostrar en qué publicaciones reaccionó un usuario.
from sqlalchemy.orm import Session
from genera_tablas import engine, Usuario, Reaccion, Publicacion

# Crear una sesión
session = Session(engine)

# Nombre del usuario a consultar
nombre_usuario = "Omar"

# Obtener el usuario
usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()

if usuario:
    print(f"Publicaciones en las que {usuario.nombre} ha reaccionado:")
    for reaccion in usuario.reacciones:
        publicacion = reaccion.publicacion
        print(f"- '{publicacion.contenido}' con reacción: {reaccion.tipo_emocion}")


session.close()