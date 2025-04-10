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

<span style="color:blue; font-weight:bold">--- MENÚ CRUD SCOTT ---</span>  
<span style="color:red; font-weight:bold">1.</span> Ver departamentos  
<span style="color:red; font-weight:bold">2.</span> Crear departamento  
<span style="color:red; font-weight:bold">3.</span> Actualizar departamento  
<span style="color:red; font-weight:bold">4.</span> Eliminar departamento  
<span style="color:red; font-weight:bold">5.</span> Ver empleados  
<span style="color:red; font-weight:bold">6.</span> Crear empleado  
<span style="color:red; font-weight:bold">7.</span> Eliminar empleado  
<span style="color:red; font-weight:bold">8.</span> Actualizar empleado  
<span style="color:red; font-weight:bold">9.</span> Insertar datos de prueba  
<span style="color:red; font-weight:bold">10.</span> Reiniciar base de datos  
<span style="color:red; font-weight:bold">0.</span> Salir  
