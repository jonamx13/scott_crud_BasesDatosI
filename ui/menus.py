import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else clear)
    print("\033c", end="")

def mostrar_menu():
    print("\n--- MENÚ CRUD SCOTT ---")
    print("1. Ver departamentos")
    print("2. Crear departamento")
    print("3. Actualizar departamento")
    print("4. Eliminar departamento")
    print("5. Ver empleados")
    print("6. Crear empleado")
    print("7. Eliminar empleado")
    print("8. Actualizar empleado")
    print("9. Insertar datos de prueba")
    print("10. Reiniciar base de datos")
    print("0. Salir")
