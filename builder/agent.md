# Agent.md - Builder

## Proyecto
Validador de registro de usuarios en Python, diseñado con separación de responsabilidades para validar los datos de entrada antes de aceptar un registro.

## ¿Qué hace este proyecto?
Este proyecto valida si la información de un usuario es válida para registrarse. Comprueba los campos principales:
- nombre de usuario
- correo electrónico
- contraseña
- confirmación de contraseña

## ¿Cómo funciona?
La lógica está centralizada en la clase `UserRegistrationValidator`, que recibe un diccionario con los datos del usuario y devuelve un resultado con dos claves:
- `is_valid`: indica si el registro es válido
- `errors`: contiene los errores detectados por campo

La validación incluye:
- longitud mínima del nombre de usuario
- formato de email válido
- longitud mínima de la contraseña
- presencia de mayúsculas, minúsculas, número y carácter especial
- coincidencia entre contraseña y confirmación

## ¿Cómo se hizo?
Se creó una estructura mínima en Python con:
- paquete `src` para la lógica del validador
- pruebas con `pytest` para verificar comportamiento válido e inválido
- configuración de importación para que el proyecto funcione correctamente desde la raíz

## Cambios realizados
- Se creó la estructura base del proyecto para validar registros de usuarios.
- Se implementó la clase `UserRegistrationValidator` con validación de nombre, email, contraseña y confirmación.
- Se añadieron pruebas unitarias para cubrir casos válidos e inválidos.
- Se configuró pytest para incluir la raíz del proyecto en el `PYTHONPATH` y resolver correctamente el paquete `src`.
- Se agregó documentación en este archivo y en los `agent.md` de cada módulo.

## Ejecución
```bash
cd /home/netebe/Documentos/SegundoDeSoftware/programacion-orientada-a-objetos/builder
python -m pip install -r requirements.txt
pytest -q
```

## Regla de documentación
Cualquier cambio, mejora, corrección o nueva funcionalidad del proyecto debe documentarse aquí y, si afecta a un módulo concreto, también en su `agent.md` correspondiente.
