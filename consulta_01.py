#Listar publicaciones de un usuario.
from sqlalchemy.orm import Session
from genera_tablas import engine, Usuario, Publicacion

# Crear una sesión
session = Session(engine)

# Nombre del usuario a consultar
nombre_usuario = "Shelley"

# Consulta usando join para aprovechar el schema
resultado = (
    session.query(Publicacion)
    .join(Usuario)
    .filter(Usuario.nombre == nombre_usuario)
    .all()
)

if resultado:
    print(f"Publicaciones de {nombre_usuario}:")
    for publicacion in resultado:
        print(f"- {publicacion.contenido}")

session.close()