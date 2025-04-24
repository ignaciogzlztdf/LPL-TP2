import json
from clases.articulo import Articulo

def cargar_articulos_json_en_lista(archivo_json="articulos.json"):
    with open(archivo_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        return [Articulo(d["titulo"], d["autor"], d["texto"]) for d in datos]