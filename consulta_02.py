#Listar las reacciones a una publicación.

from sqlalchemy.orm import Session
from genera_tablas import engine, Publicacion, Reaccion, Usuario

# Crear una sesión
session = Session(engine)

# ID de la publicación a consultar
publicacion_id = 6

# Obtener la publicación
publicacion = session.query(Publicacion).filter_by(id=publicacion_id).first()

if publicacion:
    print(f"Reacciones a la publicación: {publicacion.contenido}")
    for reaccion in publicacion.reacciones:
        usuario = reaccion.usuario
        print(f"- {reaccion.tipo_emocion} por {usuario.nombre}")

session.close()