import oracledb
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

def get_connection():
    """
    Devuelve una conexión a la base de datos Oracle usando variables de entorno.
    """
    try:
        connection = oracledb.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dsn=os.getenv("DB_DSN")
        )
        return connection
    except oracledb.Error as e:
        print("❌ Error al conectar a la base de datos:")
        print(e)
        return None
