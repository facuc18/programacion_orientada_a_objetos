

#1. ¿Qué imprime el objeto antes de sobrescribir __str__()?
#Antes de modificarlo, imprime una representación genérica heredada directamente de la clase object. Muestra el módulo, el nombre de la clase y su ubicación física en la memoria RAM (por ejemplo: <__main__.Persona object at 0x7f9b18...>).

#2. ¿Qué cambia después de implementar __str__()?
#Cambia la forma en que el objeto se presenta ante las personas. En lugar de mostrar la dirección de memoria, Python intercepta el método y ejecuta nuestro código personalizado, devolviendo una cadena de texto legible y amigable (ej: Persona: Sofía (25 años)).

#3. ¿Por qué p1 == p2 primero da False?
#Porque la implementación por defecto del método __eq__ en la clase object compara identidad (si apuntan al mismo espacio de memoria RAM). Como p1 y p2 son dos instancias creadas de forma independiente, ocupan lugares distintos en la memoria, por lo que Python los considera diferentes.

#4. ¿Por qué después puede dar True?
#Porque al sobrescribir el método __eq__, redefinimos la regla de comparación. Le enseñamos a Python a evaluar el contenido (los valores de los atributos nombre, edad y email) en lugar de la ubicación de memoria. Como los datos de ambos objetos coinciden, la comparación ahora devuelve True.

#5. ¿Qué relación tienen __eq__() y __hash__()?
#En Python existe un contrato estricto entre ambos: si dos objetos son iguales mediante == (__eq__), obligatoriamente deben generar el mismo valor de hash (__hash__).
#Si cambiamos cómo se comparan los objetos pero no modificamos su hash, Python bloquea el objeto y no nos permite usarlo en estructuras como diccionarios o conjuntos (sets). Por eso, al sobrescribir __eq__ basándonos en los atributos, debemos hacer lo mismo con __hash__.

#6. ¿Cuál sería el equivalente de getClass() de Java en Python?
#El equivalente directo es la función integrada type().
#Mientras que en Java usarías objeto.getClass(), en Python utilizás type(objeto). Si se requiere únicamente el nombre de la clase en formato de texto (String), se puede acceder mediante type(objeto).__name__