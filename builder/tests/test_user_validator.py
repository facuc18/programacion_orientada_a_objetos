from src.user_validator import UserRegistrationValidator


def test_valid_user_registration():
    data = {
        "username": "ana_01",
        "email": "ana@example.com",
        "password": "M1n!clave",
        "confirm_password": "M1n!clave",
    }

    result = UserRegistrationValidator.validate(data)

    assert result["is_valid"] is True
    assert result["errors"] == {}


def test_invalid_email_and_password_mismatch():
    data = {
        "username": "a",
        "email": "correo-invalido",
        "password": "123456",
        "confirm_password": "654321",
    }

    result = UserRegistrationValidator.validate(data)

    assert result["is_valid"] is False
    assert "username" in result["errors"]
    assert "email" in result["errors"]
    assert "password" in result["errors"]
    assert "confirm_password" in result["errors"]
