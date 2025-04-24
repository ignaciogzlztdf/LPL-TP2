from ParserHtml import ParserHtml
import json
import webbrowser
from Articulo import Articulo

# Cargar los artículos desde el archivo JSON
# Y crear una lista de objetos Articulo
with open("articulos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
    articulos = [Articulo(d["titulo"], d["autor"], d["texto"]) for d in datos]

parser = ParserHtml(articulos)
parser.crear_archivo_html_principal(parser.generar_html_principal())

# Abrir en navegador la página principal
webbrowser.open("index.html")