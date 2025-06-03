## Uso de IA generativa para el desarrollo de FutRedX


## 1. Diseño del modelo de datos con SQLAlchemy
Prompt:
"Diseña las clases ORM para una red social llamada FutRedX en SQLAlchemy. Los usuarios pueden crear publicaciones, y cada publicación puede recibir una única reacción por usuario, que tiene un tipo de emoción. Las emociones deben almacenarse en una tabla intermedia."

* Resultado:
Me ayudó a diseñar las clases Usuario, Publicacion y Reaccion, considerando las restricciones funcionales, relaciones uno a muchos y muchos a muchos, y agregando una restricción de unicidad en Reaccion.

## 2. Importación de datos desde CSV
Prompt:
"Ayúdame a importar datos desde archivos CSV a una base de datos SQLite usando SQLAlchemy. Los archivos tienen usuarios, publicaciones y reacciones. Quiero hacerlo sin usar diccionarios auxiliares, sino consultando directamente con el ORM."

* Resultado:
Generó un script de importación que lee los datos de los archivos usuarios_red_x.csv, usuarios_publicaciones.csv y usuario_publicacion_emocion.csv, y los inserta validando duplicados.

## 3. Explicación de relaciones entre clases
Prompt:
"Explícame por qué Usuario se relaciona directamente con Publicación si hay una tabla intermedia llamada Reacción."

* Resultado:
La IA explicó que hay dos relaciones: una de autoría (usuario crea publicación) y otra de interacción (usuario reacciona a publicaciones), lo cual justificaba el diseño del modelo.

## 4. Verificación del cumplimiento de requisitos
Prompt:
"¿Mi modelo cumple con los requisitos funcionales del proyecto de FutRedX?"

* Resultado:
Validó que el diseño cumplía con las relaciones necesarias, la unicidad de reacciones, y el uso adecuado de claves foráneas.

## 5. Generación de la consulta 5
Prompt:
"¿Ayudame generando esta consulta Listar todas las reacciones de tipo "alegre", "enojado", "pensativo" que sean de usuarios que cuyos nombre no inicien con vocal.?"

* Resultado:
A consulta generó una lista de reacciones de tipo "alegre", "enojado" y "pensativo", pero solo de usuarios cuyos nombres no inician con vocal. Por ejemplo:

- alegre por Bryan
- pensativo por Luis
- enojado por Pedro
- alegre por Marlon

Esto demuestra que la consulta filtra correctamente tanto por el tipo de emoción como por la condición sobre el nombre del usuario.