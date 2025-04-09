import os
from session import leer_sesion, guardar_sesion
from sql_utils import (
    ejecutar_sql_desde_archivo,
    datos_ya_existen
)
from crud import (
    leer_departamentos,
    crear_departamento,
    actualizar_departamento,
    eliminar_departamento
)

def menu():
    while True:
        print("\n--- MENÚ CRUD SCOTT ---")
        print("1. Ver departamentos")
        print("2. Crear departamento")
        print("3. Actualizar departamento")
        print("4. Eliminar departamento")
        print("5. Insertar datos de prueba")
        print("9. Reiniciar base de datos")
        print("0. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            leer_departamentos()

        elif opcion == "2":
            deptno = int(input("Número de departamento: "))
            dname = input("Nombre del departamento: ")
            loc = input("Ubicación: ")
            crear_departamento(deptno, dname, loc)

        elif opcion == "3":
            deptno = int(input("Departamento a actualizar: "))
            nuevo_nombre = input("Nuevo nombre: ")
            nueva_loc = input("Nueva ubicación: ")
            actualizar_departamento(deptno, nuevo_nombre, nueva_loc)
        
        elif opcion == "4":
            deptno = int(input("Departamento a eliminar: "))
            eliminar_departamento(deptno)

        elif opcion == "5":
            if datos_ya_existen():
                print("⚠️ Ya existen datos en la base de datos. Si deseas recargar los de prueba, reinicia primero (opción 9).")
            
            else:
                confirmar = input("¿Deseas insertar los datos de prueba? (S/N): ").strip().upper()
                if confirmar == "S":
                    ejecutar_sql_desde_archivo("sample_data.sql")

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
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla
    
    ultima = leer_sesion()
    if ultima:
        print(f"👋 Bienvenido de nuevo. Tu última sesión fue el {ultima['fecha']} desde {ultima['sistema']}.")
        print("ℹ️ Si deseas reiniciar la base de datos, ve a la opción 9.")
    else:
        print("👋 Bienvenido por primera vez.")

    menu()