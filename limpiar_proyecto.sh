#!/bin/bash

# Detectar sistema operativo
SO=$(uname)

echo "🧼 Limpiando entorno del proyecto..."

if [[ "$SO" == "Linux" || "$SO" == "Darwin" ]]; then
    # Linux o macOS
    rm -rf venv
    find . -type d -name "__pycache__" -exec rm -rf {} +
    rm -f .env
    rm -f last_session.json
    echo "✅ Proyecto limpio en $SO."
else
    echo "⚠️ Este script está pensado para Linux/macOS."
    echo "➡️ Ejecuta limpiar_proyecto.bat si estás en Windows."
fi
