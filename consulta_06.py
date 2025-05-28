# Listar usuarios que no han realizado ninguna publicación.
from sqlalchemy.orm import Session
from sqlalchemy import func
from genera_tablas import engine, Usuario, Publicacion, Reaccion

# Crear una sesión
session = Session(engine)

print("Usuarios sin publicaciones:")
usuarios_sin_publicaciones = (
    session.query(Usuario)
    .outerjoin(Usuario.publicaciones)
    .filter(Publicacion.id == None)
    .all()
)
for usuario in usuarios_sin_publicaciones:
    print(f"- {usuario.nombre}")

session.close()