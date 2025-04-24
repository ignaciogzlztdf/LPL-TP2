from clases.parser_html import ParserHtml
import json
import webbrowser
from clases.articulo import Articulo

# Cargar los artículos desde el archivo JSON
# Y crear una lista de objetos Articulo
def cargar_articulos_json(archivo_json):
    with open(archivo_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        return [Articulo(d["titulo"], d["autor"], d["texto"]) for d in datos]


archivo_json = "articulos.json"
articulos = cargar_articulos_json(archivo_json)

parser = ParserHtml(articulos)
parser.crear_archivo_html_principal(parser.generar_html_principal())

# Abrir en navegador la página principal
webbrowser.open("index.html")