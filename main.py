from session import leer_sesion, guardar_sesion
from sql_utils import ejecutar_sql_desde_archivo
import os

def menu():
    while True:
        print("\n--- MENÚ CRUD SCOTT ---")
        print("1. Ver empleados (pendiente)")
        print("2. Ver departamentos (pendiente)")
        print("9. Reiniciar base de datos")
        print("0. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("👷‍♂️ Esta opción está en desarrollo.")
        elif opcion == "2":
            print("👷‍♀️ Esta opción está en desarrollo.")
        elif opcion == "9":
            confirmar = input("⚠️ ¿Estás seguro que deseas reiniciar TODA la base de datos? (S/N): ").strip().upper()
            if confirmar == "S":
                ejecutar_sql_desde_archivo("init_db.sql")
                insertar = input("¿Deseas insertar datos de prueba? (S/N): ").strip().upper()
                if insertar == "S":
                    ejecutar_sql_desde_archivo("sample_data.sql")
        elif opcion == "0":
            print("👋 Hasta luego.")
            guardar_sesion()
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia pantalla
    ultima = leer_sesion()
    if ultima:
        print(f"👋 Bienvenido de nuevo. Tu última sesión fue el {ultima['fecha']} desde {ultima['sistema']}.")
        print("ℹ️ Si deseas reiniciar la base de datos, ve a la opción 9.")
    else:
        print("👋 Bienvenido por primera vez.")

    menu()