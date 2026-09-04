# Agent.md - Módulo src

## Módulo
`src`

## ¿Qué hace este módulo?
Este módulo agrupa la lógica principal del proyecto. En este caso, contiene el validador de registro de usuarios.

## ¿Cómo funciona?
El archivo principal es `user_validator.py` y expone la clase `UserRegistrationValidator`.

La clase implementa el método `validate(data)`, que:
- recibe un diccionario con los datos del usuario
- valida cada campo relevante
- devuelve un diccionario con `is_valid` y `errors`

## ¿Cómo se hizo?
Se construyó un módulo Python simple y claro con una sola responsabilidad: validar el registro de usuarios.

Se usó:
- `re` para comprobar patrones de email y contraseña
- `typing.Any` para manejar datos dinámicos
- un flujo secuencial de validación por campo

## Cambios realizados
- Se creó el paquete `src`.
- Se implementó `user_validator.py` con la lógica del validador.
- Se exportó la clase desde `__init__.py` para facilitar su importación.

## Nota
Cualquier cambio dentro de este módulo debe documentarse aquí.
