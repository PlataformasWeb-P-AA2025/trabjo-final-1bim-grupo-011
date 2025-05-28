# Mostrar las publicaciones que no tienen ninguna reacción.
from sqlalchemy.orm import Session
from sqlalchemy import func
from genera_tablas import engine, Usuario, Publicacion, Reaccion

# Crear una sesión
session = Session(engine)


print("\n Publicaciones sin reacciones:")
publicaciones_sin_reacciones = (
    session.query(Publicacion)
    .outerjoin(Publicacion.reacciones)
    .filter(Reaccion.id == None)
    .all()
)
for publicacion in publicaciones_sin_reacciones:
    print(f"- {publicacion.contenido}")


session.close()