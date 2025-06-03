# Obtener un reporte de reacciones en función del número de veces que fueron usadas.
from sqlalchemy.orm import Session
from genera_tablas import engine, Reaccion

# Crear una sesión
session = Session(engine)

# Obtener todas las reacciones como objetos
reacciones = session.query(Reaccion).all()

# Procesar los objetos para contar las emociones
conteo = {}
for reaccion in reacciones:
    if reaccion.tipo_emocion in conteo:
        conteo[reaccion.tipo_emocion] += 1
    else:
        conteo[reaccion.tipo_emocion] = 1

# Ordenar por cantidad descendente
reporte_ordenado = sorted(conteo.items(), key=lambda x: x[1], reverse=True)

print("Reporte de reacciones por número de usos:")
for tipo_emocion, cantidad in reporte_ordenado:
    print(f"- {tipo_emocion}: {cantidad} veces")

session.close()