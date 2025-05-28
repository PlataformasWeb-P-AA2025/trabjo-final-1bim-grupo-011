#Obtener un reporte de reacciones en función del número de veces que fueron usadas.
from sqlalchemy.orm import Session
from sqlalchemy import func
from genera_tablas import engine, Reaccion

# Crear una sesión
session = Session(engine)

# Consulta para contar el número de veces que se usó cada tipo de emoción
reporte = (
    session.query(Reaccion.tipo_emocion, func.count(Reaccion.id).label("cantidad"))
    .group_by(Reaccion.tipo_emocion)
    .order_by(func.count(Reaccion.id).desc())
    .all()
)

print("Reporte de reacciones por número de usos:")
for tipo_emocion, cantidad in reporte:
    print(f"- {tipo_emocion}: {cantidad} veces")

session.close()