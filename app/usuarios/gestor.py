from app.usuarios.validaciones import validar_nombre, validar_edad, validar_email

# Lista en memoria que almacena los usuarios registrados
_usuarios = []


def registrar_usuario(nombre: str, edad, email: str) -> dict:
    """Valida y registra un nuevo usuario. Retorna el usuario creado."""
    validar_nombre(nombre)
    validar_edad(edad)
    validar_email(email)

    # Verifica que el email no esté duplicado
    if buscar_usuario(email):
        raise ValueError(f"Ya existe un usuario registrado con el email '{email}'.")

    usuario = {
        "nombre": nombre.strip(),
        "edad": int(edad),
        "email": email.strip().lower(),
    }
    _usuarios.append(usuario)
    return usuario


def listar_usuarios() -> list:
    """Retorna la lista completa de usuarios registrados."""
    return list(_usuarios)


def buscar_usuario(email: str) -> dict | None:
    """Busca un usuario por email. Retorna el usuario o None si no existe."""
    email = email.strip().lower()
    for usuario in _usuarios:
        if usuario["email"] == email:
            return usuario
    return None