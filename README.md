## 👥 Integrantes

- Abdon Merino Llantoy  
- Daniel Rivas Castillo

Puedes visualizar la presentación del proyecto en el siguiente enlace:
👉 [Ver diapositivas](https://docs.google.com/presentation/d/16vBlCtonDUKC2kVWpjlkOFSURyTK6hgNnqVPFBGFxB8/edit?slide=id.p#slide=id.p)
# Manual de Instalación en Local del Proyecto

Este manual te guiará paso a paso para crear y configurar el proyecto en tu entorno local, incluyendo la creación del proyecto, la instalación de librerías necesarias y la ejecución de un notebook.

---

## 1. Crear el Proyecto

### 1.1 Abrir CMD (Símbolo del Sistema)

1. Abre el **CMD** o **PowerShell** en tu computadora.

2. Navega hasta la carpeta donde deseas crear el proyecto.

3. Ejecuta el siguiente comando para generar la estructura básica del proyecto:
   ```bash
   py Crear_Proyecto.py
   ```

4. **En la pantalla**, se te pedirá lo siguiente:
   - Escribe el **nombre del proyecto**: `ia_generativa`.
   - Luego, se te pedirá el **nombre del entorno virtual**: `env_ia`.

5. Espera a que el script termine de crear la estructura de carpetas y archivos del proyecto.

---

## 2. Abrir Visual Studio Code

### 2.1 Abrir la Carpeta del Proyecto en Visual Studio Code

1. Navega hasta la carpeta donde se creó el proyecto.

2. Abre la carpeta con **Visual Studio Code**. Haz clic derecho en la carpeta y selecciona **"Abrir con Visual Studio Code"**.

---

### 2.2 Seleccionar el Intérprete de Python

1. En **Visual Studio Code**, presiona **Ctrl + Shift + P** para abrir la paleta de comandos.

2. Escribe **`Python: Select Interpreter`** en la barra de búsqueda de la paleta de comandos.

3. Selecciona la opción **Python: Select Interpreter**.

4. Elige el entorno virtual que creaste anteriormente (`env_ia`).

---

## 3. Instalar las Librerías Necesarias

### 3.1 Copiar el Archivo `requirements.txt`

1. Copia el archivo **`requirements.txt`** al directorio raíz de tu proyecto.

### 3.2 Instalar las Librerías Usando `pip`

1. Abre una terminal en **Visual Studio Code** o en **CMD**.

2. Navega hasta el directorio raíz del proyecto.

3. Ejecuta el siguiente comando para instalar las librerías necesarias:
   ```bash
   pip install -r requirements.txt
   ```

---

## 4. Copiar Archivos del Proyecto

### 4.1 Copiar el Archivo `extrae.py`

1. Copia el archivo **`extrae.py`** y colócalo en la carpeta **`scripts`** de tu proyecto.

### 4.2 Copiar el Archivo `trabajo.ipynb`

1. Copia el archivo **`trabajo.ipynb`** y colócalo en la carpeta **`Notebook`** de tu proyecto.

---

## 5. Ejecutar el Notebook

### 5.1 Activar el Entorno Virtual

Si el entorno virtual no se activa automáticamente, realiza lo siguiente:

1. Abre el **CMD** dentro de la carpeta del proyecto.

2. Ejecuta el siguiente comando para activar el entorno virtual:
   ```bash
   .venv\Scriptsctivate
   ```

### 5.2 Abrir y Ejecutar el Notebook

1. Abre el archivo **`trabajo.ipynb`** en **Jupyter Notebook** o en **VSCode**.

2. Ejecuta las celdas del notebook para verificar que todo funcione correctamente.

---

## 6. Solución de Problemas con la Activación del Entorno Virtual

Si el entorno virtual no se activa correctamente en PowerShell, sigue estos pasos:

1. Abre **PowerShell** como **administrador**.

2. Ejecuta el siguiente comando para permitir la ejecución de scripts en PowerShell:
   ```bash
   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
   ```

3. Luego, activa el entorno virtual ejecutando:
   ```bash
   .venv\Scripts\Activate.ps1
   ```

---


---

## VIDEOS




---

## VIDEOS DE SEMINARIO  ABDON MERINO



https://github.com/user-attachments/assets/0488ea3d-ecf5-4b31-992a-93481bda3168



## VIDEOS DE SEMINARIO  DANIEL RIVAS 






https://github.com/user-attachments/assets/850660e8-e576-4aff-b9aa-c33f24e8f7b4






---

## VIDEOS DE SEMINARIO  ABDON MERINO




