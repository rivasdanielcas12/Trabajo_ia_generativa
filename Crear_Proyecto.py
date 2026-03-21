import os
import subprocess
import logging
from pathlib import Path
import sys

def crear_archivo(ruta, contenido=""):
    """ Crea un archivo en la ruta especificada """
    try:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(contenido)
        logging.info(f"Archivo creado correctamente: {ruta}")
    except Exception as e:
        logging.error(f"Error al crear archivo {ruta}: {e}")
        raise

def crear_estructura_y_venv(nombre_proyecto, nombre_venv=".venv"):
    """ Crea la estructura básica del proyecto y el entorno virtual """
    base = Path(nombre_proyecto).resolve()  # Usar ruta absoluta
    if base.exists():
        logging.warning(f"La carpeta '{nombre_proyecto}' ya existe. Se procederá a crear los archivos dentro.")
    else:
        base.mkdir(exist_ok=True)

    # Carpetas principales del proyecto
    carpetas = [
        "Scripts", "src/log", "src/Database", 
        "Adjuntos", "Output_Data_csv", "Bacheros", "Sql", 
        "Log/Archivos_Log", "Log/Error", "Notebook"
    ]
    for carpeta in carpetas:
        (base / carpeta).mkdir(parents=True, exist_ok=True)

    # Crear archivo .gitignore
    crear_archivo(base / ".gitignore",
                  """# Ignorar el entorno virtual
.venv/
rga/

# Ignorar archivos de configuración sensibles
.env

# Ignorar archivos de logs
Log/
*.log

# Ignorar archivos de compilación de Python
__pycache__/
*.pyc
*.pyo

# Ignorar archivos de editor (por ejemplo, VSCode, PyCharm, etc.)
.vscode/
.idea/

# Ignorar archivos de sistema
.DS_Store
Thumbs.db
""")

    # Crear archivos base
    crear_archivo(base / ".env",
                  "STRING_CONEXION_SQL=\n")
    
    crear_archivo(base / "requirements.txt",
                  "pandas\npython-dotenv\nopenpyxl\nrequests\npyodbc\nflask\n")

    crear_archivo(base / "main.py",
                  '''import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()  # Cargar variables de entorno desde el archivo .env
    print("🚀 Proyecto iniciado correctamente")
''')

    # Crear la carpeta del entorno virtual
    subprocess.run(["python", "-m", "venv", nombre_venv], cwd=base, check=True)
    
    # Instalación de librerías con la ruta absoluta de pip
    if sys.platform == "win32":  # Para Windows
        pip_path = base / nombre_venv / "Scripts" / "pip.exe"
    else:  # Para Linux/Mac
        pip_path = base / nombre_venv / "bin" / "pip"

    logging.info(f"📦 Instalando librerías desde requirements.txt usando {pip_path}...")
    
    try:
        subprocess.run([str(pip_path), "install", "-r", "requirements.txt"], cwd=base, shell=True, check=True)
        logging.info("✔ Librerías instaladas correctamente.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error al instalar librerías: {e}")
        raise
    
    logging.info("\n📁 Estructura creada correctamente y librerías instaladas.")
    logging.info(f"🎉 Proyecto completamente configurado y listo para programar")
    logging.info(f"📂 Ubicación: {base.resolve()}")

def main():
    """ Función principal para ejecutar todo en un solo comando """
    logging.info("🎯 Iniciando la creación del proyecto...")
    nombre_proyecto = input("Ingresa el nombre del proyecto: ")
    nombre_venv = input("Ingresa el nombre del entorno virtual (por defecto .venv): ") or ".venv"
    crear_estructura_y_venv(nombre_proyecto, nombre_venv)
    logging.info(
    """
    #### Pasos siguientes:
    1. Abrir visual code
    2. abre la carperta creada {nombre_proyecto}
    3. En VSCode, presiona Ctrl+Shift+P
    4.Escribe Python: 
    Select Interpreter en la paleta de comandos y selecciona la opción Python: Select Interpreter.{nombre_venv}

    """
)

if __name__ == "__main__":
    main()