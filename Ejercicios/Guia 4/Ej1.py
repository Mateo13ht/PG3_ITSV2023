import pytest

def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if any(char.isalnum() for char in password):
        return False
    return True

def test_validate_password():
    assert validate_password("Abcdef12") == True

    assert validate_password("Abc12") == False

    assert validate_password("abcdef12") == False

    assert validate_password("ABCDEF12") == False

    assert validate_password("Abcdefgh") == False

    assert validate_password("Abcdef12!") == False

    assert validate_password("") == False

    assert validate_password("Abcdef12") == True

    assert validate_password("Abc def12") == False

    assert validate_password("!@#$%^&*") == False
