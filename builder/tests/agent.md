# Agent.md - Módulo tests

## Módulo
`tests`

## ¿Qué hace este módulo?
Este módulo contiene las pruebas del proyecto. Su objetivo es verificar que el validador funcione correctamente en casos válidos e inválidos.

## ¿Cómo funciona?
Las pruebas importan la clase `UserRegistrationValidator` y ejecutan validaciones con datos de ejemplo.

Se comprueba que:
- un registro correcto devuelve `is_valid` como `True`
- un registro incorrecto devuelve `is_valid` como `False`
- los errores aparecen en los campos correspondientes

## ¿Cómo se hizo?
Se creó una prueba unitaria con `pytest` que cubre:
- caso exitoso
- caso con email inválido y contraseña distinta

## Cambios realizados
- Se creó el directorio `tests`.
- Se añadieron pruebas para validar el comportamiento del validador.
- Se configuró pytest para resolver el paquete `src` correctamente.

## Nota
Cualquier cambio en las pruebas o en la forma de validación debe documentarse aquí.
