#!/bin/bash

if [[ "$OSTYPE" == "msys" ]]; then
    echo "Activando entorno virtual en Git Bash (Windows)..."
    winpty venv/Scripts/activate.bat
elif [[ "$OSTYPE" == "linux-gnu"* ]] || [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Activando entorno virtual en Unix (Linux/macOS)..."
    source venv/bin/activate
else
    echo "Sistema operativo no soportado automáticamente. Actívalo manualmente."
fi
