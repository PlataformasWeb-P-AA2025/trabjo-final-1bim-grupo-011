#Obtener el usuario con más publicaciones.
from sqlalchemy.orm import Session
from sqlalchemy import func
from genera_tablas import engine, Usuario, Publicacion, Reaccion

# Crear una sesión
session = Session(engine)

print("\n Usuario con más publicaciones:")
usuario_mas_publicaciones = (
    session.query(Usuario, func.count(Publicacion.id).label("num_publicaciones"))
    .join(Usuario.publicaciones)
    .group_by(Usuario.id)
    .order_by(func.count(Publicacion.id).desc())
    .first()
)
if usuario_mas_publicaciones:
    usuario, cantidad = usuario_mas_publicaciones
    print(f"- {usuario.nombre} ({cantidad} publicaciones)")

session.close()
