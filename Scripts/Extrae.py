import os
import requests

MESES = {
    "Enero": "en",
    "Febrero": "fe",
    "Marzo": "ma",
    "Abril": "ab",
    "Mayo": "my",
    "Junio": "jn",
    "Julio": "jl",
    "Agosto": "ag",
    "Setiembre": "se",
    "Octubre": "oc",
    "Noviembre": "no",
    "Diciembre": "di"
}

BASE_URL = "https://intranet2.sbs.gob.pe/estadistica/financiera"

def descargar_datos(inicio=2015, fin=2025, ruta_destino="Output_Data_csv/documents"):
    # Obtener la ruta absoluta de la carpeta 'documents' con base en la ubicación de la notebook
    ruta_absoluta = os.path.abspath(ruta_destino)
    
    # Crear la carpeta destino si no existe
    os.makedirs(ruta_absoluta, exist_ok=True)

    # Listas para almacenar los archivos descargados y no descargados
    descargados = []
    no_descargados = []

    # Bucle sobre los años y meses
    for anio in range(inicio, fin + 1):
        for mes, abrev in MESES.items():
            nombre_archivo = f"C-1252-{abrev}{anio}.XLS"
            url = f"{BASE_URL}/{anio}/{mes}/{nombre_archivo}"

            try:
                # Realizar la petición HTTP
                response = requests.get(url, timeout=10)

                # Si la respuesta es exitosa (status code 200)
                if response.status_code == 200:
                    path = os.path.join(ruta_absoluta, f"{anio}_{mes}.xls")
                    with open(path, "wb") as f:
                        f.write(response.content)
                    descargados.append(f"{anio}-{mes}")  # Agregar al resumen de descargados

                else:
                    no_descargados.append(f"{anio}-{mes} (Código de estado: {response.status_code})")  # Agregar a no descargados

            except requests.exceptions.Timeout:
                no_descargados.append(f"⚠ Timeout {anio}-{mes}")
            except requests.exceptions.RequestException as e:
                no_descargados.append(f"⚠ Error al conectar {anio}-{mes}: {e}")
            except Exception as e:
                no_descargados.append(f"⚠ Error inesperado {anio}-{mes}: {e}")

    # Imprimir resumen
    print(f"\nResumen de descargas:")
    print(f"Archivos descargados: {len(descargados)}")
    print(f"Archivos no descargados: {len(no_descargados)}")

    # Mostrar detalles de los archivos descargados
    if descargados:
        print("\nArchivos descargados:")
        for archivo in descargados:
            print(f"- {archivo}")
    
    # Mostrar detalles de los archivos no descargados
    if no_descargados:
        print("\nArchivos no descargados:")
        for archivo in no_descargados:
            print(f"- {archivo}")
