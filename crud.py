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

def leer_empleados():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT EMPNO, ENAME, JOB, SAL, DEPTNO FROM EMP ORDER BY EMPNO
            """)
            empleados = cursor.fetchall()
            if not empleados:
                print("⚠️ No hay empleados registrados.")
            else:
                print("\n📋 Lista de empleados:")
                for emp in empleados:
                    print(f"  {emp[0]} - {emp[1]} ({emp[2]}) | Salario: ${emp[3]:.2f} | Departamento: {emp[4]}")
    except Exception as e:
        print("❌ Error al leer empleados:", e)

def crear_empleado():
    try:
        empno = int(input("Número de empleado: "))
        ename = input("Nombre: ")
        job = input("Puesto: ")
        mgr = input("ID del jefe (o dejar vacío): ").strip()
        mgr = int(mgr) if mgr else None
        hire_date = input("Fecha de contratación (YYYY-MM-DD): ")
        sal = float(input("Salario: "))
        comm = input("Comisión (o dejar vacío): ").strip()
        comm = float(comm) if comm else None
        deptno = int(input("Número de departamento: "))

        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO EMP (EMPNO, ENAME, JOB, MGR, HIRE_DATE, SAL, COMM, DEPTNO)
                VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'), :6, :7, :8)
            """, [empno, ename, job, mgr, hire_date, sal, comm, deptno])
            conn.commit()
            print("✅ Empleado creado exitosamente.")
    except Exception as e:
        print("❌ Error al crear empleado:", e)

def eliminar_empleado(empno):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM EMP WHERE EMPNO = :1", [empno])
            conn.commit()
            print("✅ Empleado eliminado.")
    except Exception as e:
        print("❌ Error al eliminar empleado:", e)

def actualizar_salario(empno, nuevo_salario):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE EMP SET SAL = :1 WHERE EMPNO = :2", [nuevo_salario, empno])
            conn.commit()
            print("✅ Salario actualizado.")
    except Exception as e:
        print("❌ Error al actualizar salario:", e)
