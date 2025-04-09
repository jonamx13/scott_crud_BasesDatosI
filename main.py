import os
from session import leer_sesion, guardar_sesion
from db.sql_utils import ejecutar_sql_desde_archivo
from ui.menus import mostrar_menu
from services.dept_service import (
    leer_departamentos,
    crear_departamento,
    actualizar_departamento,
    eliminar_departamento
)
from services.emp_service import (
    leer_empleados,
    crear_empleado,
    eliminar_empleado,
    actualizar_empleado
)

def datos_ya_existen():
    from db.db_config import get_connection
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM DEPT")
            total = cursor.fetchone()[0]
            return total > 0
    except:
        return False

def menu():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        match opcion:
            case "1": leer_departamentos()
            case "2": crear_departamento()
            case "3": actualizar_departamento()
            case "4": eliminar_departamento()
            case "5": leer_empleados()
            case "6": crear_empleado()
            case "7": eliminar_empleado()
            case "8": actualizar_empleado()
            case "9":
                if datos_ya_existen():
                    print("⚠️ Ya existen datos en la base de datos. Si deseas recargar los de prueba, reinicia primero (opción 10).")
                else:
                    confirmar = input("¿Deseas insertar los datos de prueba? (S/N): ").strip().upper()
                    if confirmar == "S":
                        ejecutar_sql_desde_archivo("sample_data.sql")
            case "10":
                confirmar = input("⚠️ ¿Estás seguro que deseas reiniciar TODA la base de datos? (S/N): ").strip().upper()
                if confirmar == "S":
                    ejecutar_sql_desde_archivo("init_db.sql")
                    insertar = input("¿Deseas insertar datos de prueba? (S/N): ").strip().upper()
                    if insertar == "S":
                        ejecutar_sql_desde_archivo("sample_data.sql")
            case "0":
                print("👋 Hasta luego.")
                guardar_sesion()
                break
            case _:
                print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar consola

    ultima = leer_sesion()
    if ultima:
        print(f"👋 Bienvenido de nuevo. Tu última sesión fue el {ultima['fecha']} desde {ultima['sistema']}.")
        print("ℹ️ Si deseas reiniciar la base de datos, ve a la opción 10.")
    else:
        print("👋 Bienvenido por primera vez.")

    menu()
