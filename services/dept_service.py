from db.db_config import get_connection

def leer_departamentos():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM DEPT ORDER BY DEPTNO")
            departamentos = cursor.fetchall()
            if not departamentos:
                print("⚠️ No hay departamentos registrados.")
            else:
                print("\n📋 Lista de departamentos:")
                for dept in departamentos:
                    print(f"  {dept[0]} - {dept[1]} ({dept[2]})")
    except Exception as e:
        print("❌ Error al leer departamentos:", e)

def crear_departamento():
    try:
        print("\n🆕 Crear nuevo departamento")
        deptno = int(input("Número de departamento (ej. 50): "))
        dname = input("Nombre del departamento (ej. MARKETING): ")
        loc = input("Ubicación (ej. MONTERREY): ")

        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO DEPT (DEPTNO, DNAME, LOC)
                VALUES (:1, :2, :3)
            """, [deptno, dname, loc])
            conn.commit()
            print("✅ Departamento creado exitosamente.")
    except Exception as e:
        print("❌ Error al crear departamento:", e)

def actualizar_departamento():
    leer_departamentos()
    try:
        deptno = int(input("\nID del departamento a actualizar: "))
        nuevo_nombre = input("Nuevo nombre: ")
        nueva_loc = input("Nueva ubicación: ")

        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE DEPT
                SET DNAME = :1, LOC = :2
                WHERE DEPTNO = :3
            """, [nuevo_nombre, nueva_loc, deptno])
            conn.commit()
            print("✅ Departamento actualizado.")
    except Exception as e:
        print("❌ Error al actualizar departamento:", e)

def eliminar_departamento():
    leer_departamentos()
    try:
        deptno = int(input("\nID del departamento a eliminar: "))
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM DEPT WHERE DEPTNO = :1", [deptno])
            conn.commit()
            print("✅ Departamento eliminado.")
    except Exception as e:
        print("❌ Error al eliminar departamento:", e)
