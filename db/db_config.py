import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        dsn = os.getenv("DB_DSN")
        return oracledb.connect(user=user, password=password, dsn=dsn)
    except Exception as e:
        print("❌ Error al conectar a la base de datos:")
        print(e)
        return None
