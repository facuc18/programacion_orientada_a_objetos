"""Validador de registros de usuarios."""

from __future__ import annotations

import re
from typing import Any


class UserRegistrationValidator:
    """Valida los datos requeridos para registrar un usuario."""

    @staticmethod
    def validate(data: dict[str, Any]) -> dict[str, Any]:
        """Valida y devuelve el resultado del registro.

        Returns:
            dict: {"is_valid": bool, "errors": {campo: mensaje}}
        """
        errors: dict[str, str] = {}

        username = data.get("username", "")
        email = data.get("email", "")
        password = data.get("password", "")
        confirm_password = data.get("confirm_password", "")

        if not isinstance(username, str) or len(username.strip()) < 3:
            errors["username"] = "El nombre de usuario debe tener al menos 3 caracteres."
        elif not re.fullmatch(r"[A-Za-z0-9_]+", username):
            errors["username"] = "El nombre de usuario solo puede contener letras, números y guion bajo."

        if not isinstance(email, str) or not re.fullmatch(
            r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
            email,
        ):
            errors["email"] = "El correo electrónico no es válido."

        if not isinstance(password, str):
            errors["password"] = "La contraseña es obligatoria."
        else:
            if len(password) < 8:
                errors["password"] = "La contraseña debe tener al menos 8 caracteres."
            elif not re.search(r"[A-Z]", password):
                errors["password"] = "La contraseña debe incluir al menos una mayúscula."
            elif not re.search(r"[a-z]", password):
                errors["password"] = "La contraseña debe incluir al menos una minúscula."
            elif not re.search(r"\d", password):
                errors["password"] = "La contraseña debe incluir al menos un número."
            elif not re.search(r"[^A-Za-z0-9]", password):
                errors["password"] = "La contraseña debe incluir al menos un carácter especial."

        if not isinstance(confirm_password, str) or confirm_password != password:
            errors["confirm_password"] = "La confirmación de contraseña no coincide."

        return {
            "is_valid": not errors,
            "errors": errors,
        }
