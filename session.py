import json
import platform
from datetime import datetime
import os

SESSION_FILE = "last_session.json"

def sistema_legible():
    sistemas = {
        "Windows": "Windows",
        "Linux": "Linux",
        "Darwin": "macOS"
    }
    return sistemas.get(platform.system(), platform.system())

def guardar_sesion():
    """
    Guarda la fecha y hora actuales, junto con el sistema operativo.
    """
    data = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "sistema": sistema_legible()
    }
    try:
        with open(SESSION_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f)
    except Exception as e:
        print("❌ No se pudo guardar la sesión:", e)

def leer_sesion():
    """
    Lee la última sesión guardada. Si no existe, devuelve None.
    """
    if not os.path.exists(SESSION_FILE):
        return None
    try:
        with open(SESSION_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print("⚠️ No se pudo leer la sesión anterior:", e)
        return None
