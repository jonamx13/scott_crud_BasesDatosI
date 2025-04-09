from db.db_config import get_connection
from services.dept_service import leer_departamentos

def leer_empleados():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT EMPNO, ENAME, JOB, SAL, DEPTNO FROM EMP ORDER BY EMPNO")
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
    leer_departamentos()
    try:
        print("\n🆕 Crear nuevo empleado")
        empno = int(input("Número de empleado (ej. 1234): "))
        ename = input("Nombre (máx 10 caracteres): ")[:10]
        job = input("Puesto (máx 9 caracteres): ")[:9]
        mgr = input("ID del jefe (opcional, ENTER si ninguno): ").strip()
        mgr = int(mgr) if mgr else None
        hire_date = input("Fecha de contratación (YYYY-MM-DD): ")
        sal = float(input("Salario: "))
        comm = input("Comisión (opcional): ").strip()
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

def eliminar_empleado():
    leer_empleados()
    try:
        empno = int(input("\nID del empleado a eliminar: "))
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM EMP WHERE EMPNO = :1", [empno])
            conn.commit()
            print("✅ Empleado eliminado.")
    except Exception as e:
        print("❌ Error al eliminar empleado:", e)

def actualizar_empleado():
    leer_empleados()
    try:
        empno = int(input("\nID del empleado a actualizar: "))
        ename = input("Nuevo nombre (máx 10 caracteres): ")[:10]
        job = input("Nuevo puesto (máx 9 caracteres): ")[:9]
        mgr = input("Nuevo ID de jefe (ENTER si ninguno): ").strip()
        mgr = int(mgr) if mgr else None
        hire_date = input("Nueva fecha de contratación (YYYY-MM-DD): ")
        sal = float(input("Nuevo salario: "))
        comm = input("Nueva comisión (ENTER si no aplica): ").strip()
        comm = float(comm) if comm else None
        deptno = int(input("Nuevo número de departamento: "))

        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE EMP
                SET ENAME = :1, JOB = :2, MGR = :3, HIRE_DATE = TO_DATE(:4, 'YYYY-MM-DD'),
                    SAL = :5, COMM = :6, DEPTNO = :7
                WHERE EMPNO = :8
            """, [ename, job, mgr, hire_date, sal, comm, deptno, empno])
            conn.commit()
            print("✅ Empleado actualizado.")
    except Exception as e:
        print("❌ Error al actualizar empleado:", e)
