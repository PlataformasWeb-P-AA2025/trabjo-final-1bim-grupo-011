#Listar las publicaciones que tienen al menos 3 reacciones.

from sqlalchemy.orm import Session
from sqlalchemy import func
from genera_tablas import engine, Usuario, Publicacion, Reaccion

# Crear una sesión
session = Session(engine)

print("\nPublicaciones con al menos 3 reacciones:")
publicaciones_con_3_reacciones = (
    session.query(Publicacion)
    .join(Publicacion.reacciones)
    .group_by(Publicacion.id)
    .having(func.count(Reaccion.id) >= 3)
    .all()
)
for publicacion in publicaciones_con_3_reacciones:
    print(f"- {publicacion.contenido}")

session.close()