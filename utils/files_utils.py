import os

def guardar_en_archivo_html(ruta:str, html:str):
    # Guardo el HTML en un archivo
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write(html)


def crear_carpeta_html_articulos():
    # Me aseguro de que la carpeta exista, si no existe la creo
    carpeta_html_articulos = "html_articulos"
    if not os.path.exists(carpeta_html_articulos):
        os.makedirs(carpeta_html_articulos, exist_ok=True)