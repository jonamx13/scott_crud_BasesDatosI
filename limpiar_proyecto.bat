@echo off
echo 🧼 Limpiando entorno del proyecto...

rmdir /s /q venv
del /f /q .env
del /f /q last_session.json
for /r %%i in (__pycache__) do (
    if exist "%%i" rmdir /s /q "%%i"
)

echo ✅ Proyecto limpio en Windows.
pause
