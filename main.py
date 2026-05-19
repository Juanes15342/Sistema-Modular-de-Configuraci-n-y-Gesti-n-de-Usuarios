from config.settings import APP_NAME, APP_VERSION, ADMIN_USER
from app.usuarios import registrar_usuario, listar_usuarios, buscar_usuario
 
 
def mostrar_encabezado():
    print("\n" + "=" * 45)
    print(f"  {APP_NAME}  v{APP_VERSION}")
    print(f"  Usuario administrador: {ADMIN_USER}")
    print("=" * 45)
 
 
def mostrar_menu():
    print("\n¿Qué deseas hacer?")
    print("  1. Registrar usuario")
    print("  2. Listar usuarios")
    print("  3. Buscar usuario por email")
    print("  4. Salir")
 
 
def opcion_registrar():
    print("\n--- Registro de nuevo usuario ---")
    nombre = input("Nombre: ")
    edad   = input("Edad:   ")
    email  = input("Email:  ")
    try:
        usuario = registrar_usuario(nombre, edad, email)
        print(f"\n✔ Usuario '{usuario['nombre']}' registrado exitosamente.")
    except ValueError as e:
        print(f"\n✘ Error al registrar: {e}")
 
 
def opcion_listar():
    print("\n--- Lista de usuarios ---")
    usuarios = listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados aún.")
        return
    for i, u in enumerate(usuarios, start=1):
        print(f"  {i}. {u['nombre']} | Edad: {u['edad']} | Email: {u['email']}")
 
 
def opcion_buscar():
    print("\n--- Buscar usuario ---")
    email = input("Ingresa el email a buscar: ")
    try:
        usuario = buscar_usuario(email)
        if usuario:
            print(f"\n✔ Usuario encontrado:")
            print(f"   Nombre : {usuario['nombre']}")
            print(f"   Edad   : {usuario['edad']}")
            print(f"   Email  : {usuario['email']}")
        else:
            print(f"\n✘ No se encontró ningún usuario con el email '{email}'.")
    except Exception as e:
        print(f"\n✘ Error en la búsqueda: {e}")
 
 
def main():
    mostrar_encabezado()
    while True:
        mostrar_menu()
        opcion = input("\nOpción: ").strip()
        if opcion == "1":
            opcion_registrar()
        elif opcion == "2":
            opcion_listar()
        elif opcion == "3":
            opcion_buscar()
        elif opcion == "4":
            print("\nHasta luego 👋\n")
            break
        else:
            print("\n✘ Opción no válida. Intenta de nuevo.")
 
 
if __name__ == "__main__":
    main()