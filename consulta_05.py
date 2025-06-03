from sqlalchemy.orm import Session
from genera_tablas import engine, Reaccion, Usuario

# Crear una sesión
session = Session(engine)

# Tipos de emoción a filtrar
tipos_emocion = ["alegre", "enojado", "pensativo"]

# Letras vocales (para filtrar nombres que NO empiezan por estas)
vocales = ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú')

# Armar condiciones para cada vocal (nombre no comienza con esa vocal)
from sqlalchemy import or_, and_, not_

condiciones = and_(
    *[~Usuario.nombre.ilike(f"{v}%") for v in vocales]
)

# Consulta ajustada para SQLite
reacciones = (session.query(Reaccion)
    .join(Reaccion.usuario)
    .filter(
        Reaccion.tipo_emocion.in_(tipos_emocion),
        condiciones
    )
    .all()
)

print('Reacciones filtradas:')
for reaccion in reacciones:
    print(f"- {reaccion.tipo_emocion} por {reaccion.usuario.nombre}")

session.close()
