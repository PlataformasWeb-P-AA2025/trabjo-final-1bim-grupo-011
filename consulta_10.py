# Mostrar los tipos de reacciones que ha usado cada usuario.
from sqlalchemy.orm import Session
from sqlalchemy import func
from genera_tablas import engine, Usuario, Publicacion, Reaccion

# Crear una sesión
session = Session(engine)


print("\nTipos de reacciones usadas por cada usuario:")
usuarios = session.query(Usuario).all()
for usuario in usuarios:
    tipos = {reaccion.tipo_emocion for reaccion in usuario.reacciones}
    if tipos:
        print(f"- {usuario.nombre}: {', '.join(tipos)}")

      