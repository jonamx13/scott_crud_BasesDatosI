# 🐍 Proyecto CRUD con Oracle y Python – Esquema SCOTT

Este proyecto es una aplicación de consola en Python que realiza operaciones **CRUD** (Crear, Leer, Actualizar, Eliminar) sobre las tablas `DEPT` y `EMP`, inspiradas en el **SCOTT Schema** clásico de Oracle.

Funciona en **Windows, Linux y macOS**, sin necesidad de instalar Oracle Client, gracias al **modo Thin** del driver `oracledb`.

---

## 🚀 Requisitos
- Python 3.10 o superior ✅  
- Git ✅  
- Oracle Database local (puede ser Oracle XE) ✅  
- Usuario con permisos (puede ser `SYSTEM`, no es obligatorio usar `SCOTT`) ✅
---

## 📦 Instalación y configuración

### 1. Clona este repositorio

```bash
git clone https://github.com/tuusuario/scott_crud.git
cd scott_crud
```

### 2. Crea y activa un entorno virtual
```bash
## Primero creamos el entorno virtual
python -m venv venv

## Luego lo activamos según nuestro sistema operativo
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Instala las dependencias
Creamos un archivo `.env` en la raíz de nuestro proyecto
```bash
# Ingresa tu usuario que usas en Oracle
DB_USER=**TU_USUARIO** // Ejemplo -> DB_USER=SYSTEM

# Ingresa tu contraseña que usas en Oracle
DB_PASSWORD=**TU_CONTRASEÑA** // Ejemplo -> DB_PASSWORD=password

# nombre del servicio para Oracle XE
DB_DSN=**TU_SERVICIO** //Ejemplo -> DB_DSN=localhost/XEPDB1
```
> Asegurate de que el `DSN` sea correcto. si usas **Oracle XE**, problablemente sea `localhost/XEPDB1`

## 🧠 Estructura del proyecto
```bash
scott_crud/
│
├── db/
│   ├── config.py         ← Conexión a "Oracle"
│   └── sql_utils.py      ← Ejecutar scripts "SQL"
│
├── services/
│   ├── dept_service.py   ← "CRUD" de "DEPT"
│   └── emp_service.py    ← "CRUD" de "EMP"
│
├── ui/
│   └── menus.py          ← Menú principal y limpieza
│
├── session.py            ← Control de sesiones (fecha y sistema operativo)
├── main.py               ← "App principal (entry point)"
├── init_db.sql           ← Script para crear las tablas
├── sample_data.sql       ← Datos de prueba
├── .env                  ← Tus credenciales "(NO subir a GitHub)"
├── .gitignore
├── limpiar.sh            ← Script limpieza "Linux/macOS"
├── limpiar_proyecto.bat  ← Script limpieza "Windows"
└── README.md

```

## 🧪 Uso

### 1. Ejecuta la app

```bash
python main.py
```
### 2. Menú principal

--- MENÚ CRUD SCOTT ---
1. Ver departamentos
2. Crear departamento
3. Actualizar departamento
4. Eliminar departamento
5. Ver empleados
6. Crear empleado
7. Eliminar empleado
8. Actualizar empleado
9. Insertar datos de prueba
10. Reiniciar base de datos
0. Salir


## 🧼 Limpieza del proyecto

Para eliminar todo el entorno virtual, variables y cachés locales:

### Linux🐧/macOS🍎

```bash
./limpiar.sh
```
### Windows ⊞

```bash
limpiar_proyecto.bat
```

Esto eliminará:
* `venv/`
* `.env`
* `last_session.json`
*  Carpetas `__pycache__`

## 🎯 Funciones destacadas
* ✅ Menús limpios con navegación por pantalla
* ✅ Consola se reinicia entre acciones para no saturar el flujo
* ✅ Persistencia de sesión con fecha y sistema operativo detectado(`Windows`, `Linux`, `MacOS`)
* ✅ Valores actuales sugeridos al actualizar datos
* ✅ Modularización real: servicios, UI, BD, sesiones

## 🛠 Tecnología usada

* Python 3.11
* Oracle Database (modo Thin)
* `oracledb` (driver oficial de Oracle para Python)
* `dotenv` para variables de entorno
* ANSI Escape Codes para limpiar pantalla en consola

## 🧾 Créditos
**Materia:** Bases de Datos I
**Asesor:** Ricardo Ramón Torres Knight
**Alumno:** Jonathan Eduardo Olivas Meixueiro
**Matricula:** 240694
**Fecha de entrega:** 10/Abril/2025

## 🚫 Notas


* **NO** subas tu `.env` ni `last_session` a ningún repositorio.
* El proyecto está preparado para ser multiplataforma, testeado en (Windows⊞, MacOS🍎 y Linux🐧).