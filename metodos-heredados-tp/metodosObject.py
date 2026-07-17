class Persona:
    def __init__(self , nombre , edad , email):
        self.nombre = nombre
        self.edad = edad
        self.email = email

    #1. Que se ve al usar print() o str()
    def __str__(self):
        return f"Persona: {self.nombre} ({self.edad} años)"
    
    #2. Que se ve al usar repr() (formato tecnico)
    def __repr__(self):
        return f"Persona(nombre='{self.nombre}' , edad={self.edad} , email='{self.email}')"
    
    #3. como se comparan con == (por contenido, no por memoria)
    def __eq__(self,otro):
        if not isinstance(otro,Persona) :
            return False
        return self.nombre == otro.nombre and self.edad == otro.edad and self.email == otro.email

    #4. generar el hash basado en sus datos 
    def __hash__(self):
        return hash((self.nombre, self.edad, self.email))

# === PRUEBAS EN ARCHIVOS MODIFICADO ===

p1 = Persona("Sofia",25,"sofia@email.com")

p1 = Persona("Sofia",25,"sofia@email.com")

print(" --- RESULTADOS DEL TP (MODIFICADO) --- ")

#Probar impresion directa y str()
#EXPLICACION: Ahora imprime: "Persona: Sofia(25 años)"
#Esto pasa porque python intercepta el print y ejecuta NUESTRO metodo __str__
print(f"Impresion directa: {p1}")
print(f"Usando str(): {str(p1)}")

# Probar repr()
# EXPLICACIÓN: Ahora imprime: "Persona(nombre='Sofía', edad=25, email='sofia@email.com')".
# Nos da una representación técnica y limpia del objeto, ideal para desarrolladores.
print(f"Usando repr(): {repr(p1)}")

# Probar comparación
# EXPLICACIÓN: ¡Ahora da TRUE! Nuestro método __eq__ le enseñó a Python a ignorar la memoria RAM
# y a comparar los strings y números de adentro (nombre, edad, email). Como son iguales, da True.
print(f"¿Son iguales p1 y p2?: {p1 == p2}")

# Probar hash
# EXPLICACIÓN: ¡Ahora los dos hashes son EXACTAMENTE EL MISMO NÚMERO!
# Al modificar __hash__, obligamos a Python a calcular el número usando sus datos. 
# Como p1 y p2 tienen los mismos datos, generan el mismo hash (regla fundamental de Python).
print(f"Hash de p1: {hash(p1)}")
print(f"Hash de p2: {hash(p2)}")

# Probar type()
# EXPLICACIÓN: Sigue imprimiendo <class '__main__.Persona'>. Su tipo no cambia por modificar métodos.
print(f"Tipo de objeto: {type(p1)}")

# Probar dir()
# EXPLICACIÓN: La lista de métodos va a ser similar a la anterior, pero con una diferencia clave:
# los métodos '__str__', '__repr__', '__eq__' y '__hash__' que aparecen ahí ahora apuntan
# a las funciones que vos mismo escribiste en el código, reemplazando a las de 'object'.
print("\n--- Métodos contenidos en el objeto (dir) ---")
print(dir(p1))