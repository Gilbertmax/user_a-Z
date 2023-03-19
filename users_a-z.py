import sqlite3

#Conectar a la base de datos (crea la base de datos si no existe)
conn = sqlite3.connect('usuarios.db')

#Tabla de usuarios
conn.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (nombre TEXT, edad INTEGER, email TEXT)''')

#Usuarios de ejemplo
conn.execute("INSERT INTO usuarios (nombre, edad, email) VALUES ('Ana', 20, 'ana@example.com')")
conn.execute("INSERT INTO usuarios (nombre, edad, email) VALUES ('Carlos', 25, 'carlos@example.com')")
conn.execute("INSERT INTO usuarios (nombre, edad, email) VALUES ('Beto', 17, 'beto@example.com')")
conn.execute("INSERT INTO usuarios (nombre, edad, email) VALUES ('Daniel', 30, 'daniel@example.com')")

#Ordena los usuarios alfabéticamente
cursor = conn.execute("SELECT * FROM usuarios ORDER BY nombre")

#Verifica si algún usuario es menor de edad y lanzar un error si es así
for row in cursor:
    if row[1] < 18:
        raise ValueError("El usuario {} es menor de edad.".format(row[0]))
    print(row[0], row[1], row[2])

# Cerrar la conexión a la base de datos
conn.close()
