def validar_nombre(nombre: str) -> None:
    """Valida que el nombre no esté vacío ni tenga solo espacios."""
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")
    if any(car.isdigit() for car in nombre):
        raise ValueError("El nombre no puede contener números.")


def validar_edad(edad) -> None:
    """Valida que la edad sea un número entero positivo y razonable."""
    try:
        edad_int = int(edad)
    except (ValueError, TypeError):
        raise ValueError("La edad debe ser un número entero.")
    if edad_int < 0:
        raise ValueError("La edad no puede ser negativa.")
    if edad_int > 120:
        raise ValueError("La edad ingresada no es válida (máximo 120).")


def validar_email(email: str) -> None:
    """Valida que el email tenga un formato básico correcto."""
    if not email or "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError("El email ingresado no es válido.")