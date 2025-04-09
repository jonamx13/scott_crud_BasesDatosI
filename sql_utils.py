from db_config import get_connection

def datos_ya_existen():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM DEPT")
            total = cursor.fetchone()[0]
            return total > 0
    except Exception:
        return False

def ejecutar_sql_desde_archivo(ruta_sql):
    """
    Ejecuta un archivo .sql completo (usando separadores de comandos por ';').
    """
    try:
        with open(ruta_sql, 'r', encoding='utf-8') as archivo:
            sql_script = archivo.read()

        # Separar los comandos por ';', pero mantener los que son válidos
        comandos = [cmd.strip() for cmd in sql_script.split(';') if cmd.strip()]

        with get_connection() as conn:
            cursor = conn.cursor()
            for comando in comandos:
                try:
                    cursor.execute(comando)
                except Exception as inner_e:
                    print(f"⚠️ Error en comando:\n{comando}\n→ {inner_e}")
            conn.commit()
        print("✅ Script ejecutado correctamente:", ruta_sql)
    except Exception as e:
        print("❌ Error al ejecutar el script SQL:", e)