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
Primero creamos el entorno virtual
```bash
python -m venv venv
```
Luego lo activamos según nuestro sistema operativo
#### ⊞ Windows:
```bash
## CMD
venv\Scripts\activate.bat

## Powershell
venv\Scripts\Activate.ps1

## Git bash (opción 1)
winpty venv/Scripts/activate.bat

## Git bash (opción 2)
source venv/Scripts/activate
```

#### 🍎macOS/ 🐧Linux:
```bash
source venv/bin/activate
```
### 3. Instala las dependencias
```bash
pip install -r requirements.txt
```

### 4. Crea un archivo `.env`

Creamos un archivo `.env` en la raíz de nuestro proyecto
```bash
# Ingresa tu usuario que usas en Oracle
DB_USER=**TU_USUARIO** // Ejemplo -> DB_USER=SYSTEM

# Ingresa tu contraseña que usas en Oracle
DB_PASSWORD=**TU_CONTRASEÑA** // Ejemplo -> DB_PASSWORD=password

# nombre del servicio para Oracle XE
DB_DSN=**TU_SERVICIO** //Ejemplo -> DB_DSN=localhost/XEPDB1
```
> ⚠️ Asegúrate de que el `DB_DSN` sea correcto. si usas **Oracle XE**, problablemente sea `localhost/XEPDB1`

---

## 🔌 Conexión en Oracle Database / SQL Developer

Este proyecto se conecta directamente a la base de datos Oracle desde Python usando las variables definidas en el archivo `.env`. Sin embargo, puedes verificar manualmente que todo esté funcionando correctamente usando **SQL Developer** u otro cliente Oracle.

### ▶️ Pasos para conectar en SQL Developer:

1. Abre **SQL Developer**
2. Crea una nueva conexión:

- **Nombre de conexión:** `scott_crud` (puede ser cualquiera)
- **Usuario:** `SYSTEM` (o el que pusiste en tu `.env`)
- **Contraseña:** la que configuraste al instalar Oracle
- **Tipo:** Básico
- **Host:** `localhost`
- **Puerto:** `1521`
- **SID:** `xe` (Si configuramos el ***Nombre del servicio*** dejamos este vacío)
- **Nombre del Servicio:** `XEPDB1` (nombre de servicio típico para **Oracle XE**) (Si configuramos el ***SID*** dejamos este vacío)
- Marca "Guardar contraseña"

3. Haz clic en **Probar conexión**

Si todo está correcto, verás el mensaje:

Estado: Correcto


💡 Esto confirma que tus credenciales `.env` están bien configuradas y que tu base de datos está activa.


## 🧠 Estructura del proyecto
```bash
scott_crud/
│
├── db/
│   ├── db_config.py         ← Conexión a "Oracle"
│   └── sql_utils.py      ← Ejecutar scripts "SQL"
│
├── services/
│   ├── dept_service.py   ← "CRUD" de "DEPT"
│   └── emp_service.py    ← "CRUD" de "EMP"
│
├── ui/
│   └── menus.py          ← Menú principal y limpieza
│
├── main.py               ← "App principal (entry point)"
├── session.py            ← Control de sesiones (fecha y sistema operativo)
├── init_db.sql           ← Script para crear las tablas
├── sample_data.sql       ← Datos de prueba
├── requirements.txt      ← Listado de dependencias para entorno virtual (venv)
├── activate_env.sh       ← Script para activar entorno virtual (venv)
├── limpiar_proyecto.bat  ← Script para limpiar y reiniciar proyecto en "Windows"
├── limpiar_proyecto.sh   ← Script para limpiar y reiniciar proyecto en "MacOS/Linux"
├── .env                  ← Credenciales “(NO subir a repositorio remoto)”
├── .gitignore            ← Exclusión de archivos locales y de caché
└── README.md             ← Documentación del proyecto
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
./limpiar_proyecto.sh
```
### Windows ⊞

```bash
./limpiar_proyecto.bat
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
* ✅ Modularización: Servicios, UI(Interfaz de usuario), Bases de Datos, Sesiones

## 🛠 Tecnología usada

* Python 3.11
* Oracle Database (modo Thin)
* `oracledb` (driver oficial de Oracle para Python)
* `dotenv` para variables de entorno
* ANSI Escape Codes para limpiar pantalla en consola

## 🧾 Créditos
- **Materia:** Bases de Datos I
- **Asesor:** Ricardo Ramón Torres Knight
- **Alumno:** Jonathan Eduardo Olivas Meixueiro
- **Matricula:** 240694
- **Fecha de entrega:** 10/Abril/2025

## 🚫 Notas


* **NO** subas tu `.env` ni `last_session` a ningún repositorio.
* El proyecto está preparado para ser multiplataforma, testeado en (Windows⊞, MacOS🍎 y Linux🐧).
