class Persona:
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email

# === PRUEBAS EN ARCHIVO SIN MODIFICAR ===
p1 = Persona("Sofía", 25, "sofia@email.com")
p2 = Persona("Sofía", 25, "sofia@email.com")

print("--- RESULTADOS DEL TP (SIN MODIFICAR) ---")

# Probar impresión directa y str()
# EXPLICACIÓN: Como no hay __str__, Python usa la versión heredada de 'object'.
# Va a imprimir algo como: <__main__.Persona object at 0x000001A2B3>.
# Muestra el nombre de la clase y su ubicación física en la memoria RAM.
print(f"Impresión directa: {p1}")
print(f"Usando str(): {str(p1)}")

# Probar repr()
# EXPLICACIÓN: Al no estar modificado, hace exactamente lo mismo que str():
# Muestra la dirección de memoria (<__main__.Persona object at 0x... >).
print(f"Usando repr(): {repr(p1)}")

# Probar comparación
# EXPLICACIÓN: Va a dar FALSE. ¿Por qué? Porque 'object' compara identidades (direcciones de memoria).
# Como 'p1' y 'p2' se crearon por separado, ocupan dos lugares distintos en la RAM,
# así que para Python son "distintos" aunque tengan los mismos datos.
print(f"¿Son iguales p1 y p2?: {p1 == p2}")

# Probar hash
# EXPLICACIÓN: Va a dar dos números enteros gigantescos y COMPLETAMENTE DIFERENTES.
# Por defecto, el hash se calcula usando la dirección de memoria del objeto.
print(f"Hash de p1: {hash(p1)}")
print(f"Hash de p2: {hash(p2)}")

# Probar type()
# EXPLICACIÓN: Imprime <class '__main__.Persona'>. Esto no cambia, te dice de qué tipo es.
print(f"Tipo de objeto: {type(p1)}")

# Probar dir()
# EXPLICACIÓN: Va a imprimir una lista enorme. Vas a ver métodos como '__str__', '__eq__', etc.
# Pero ojo: todos esos métodos son los que Python heredó por defecto de 'object', no los tuyos.
print("\n--- Métodos contenidos en el objeto (dir) ---")
print(dir(p1))