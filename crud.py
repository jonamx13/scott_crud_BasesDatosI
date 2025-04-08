from db_config import get_connection

def crear_departamento(deptno, dname, loc):
    """
    Crea un nuevo departamento en la tabla DEPT.
    """
    try:
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

def leer_departamentos():
    """
    Muestra todos los departamentos.
    """
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

def actualizar_departamento(deptno, nuevo_nombre, nueva_loc):
    """
    Actualiza los datos de un departamento existente.
    """
    try:
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

def eliminar_departamento(deptno):
    """
    Elimina un departamento (solo si no tiene empleados relacionados).
    """
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM DEPT WHERE DEPTNO = :1", [deptno])
            conn.commit()
            print("✅ Departamento eliminado.")
    except Exception as e:
        print("❌ No se pudo eliminar el departamento. Verifica que no tenga empleados asignados.")
