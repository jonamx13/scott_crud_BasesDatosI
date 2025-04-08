from db_config import get_connection

def ejecutar_sql_desde_archivo(ruta_sql):
    """
    Ejecuta un archivo .sql línea por línea.
    """
    try:
        with open(ruta_sql, 'r', encoding='utf-8') as archivo:
            sql_script = archivo.read()

        comandos = sql_script.split(';')
        with get_connection() as conn:
            cursor = conn.cursor()
            for comando in comandos:
                comando = comando.strip()
                if comando:
                    cursor.execute(comando)
            conn.commit()
        print("✅ Script ejecutado correctamente:", ruta_sql)
    except Exception as e:
        print("❌ Error al ejecutar el script SQL:", e)
