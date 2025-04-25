import json
from clases.articulo import Articulo

def cargar_articulos_json_en_lista(archivo_json="articulos.json"):
    with open(archivo_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        return [Articulo(d["titulo"], d["autor"], d["texto"]) for d in datos]


def contar_articulos_por_autor(articulos):
    contador = {}
    for articulo in articulos:
        autor = articulo.autor
        if autor in contador:
            contador[autor] += 1
        else:
            contador[autor] = 1
    return contador


def obtener_autores_por_letra(articulos):
    autores_por_letra = {}

    letras = [chr(num_letra) for num_letra in range(ord('A'), ord('Z') + 1)]

    autores_unicos = []
    autores_vistos = set()
    for articulo in articulos:
        if articulo.autor not in autores_vistos:
          autores_unicos.append(articulo.autor)
          autores_vistos.add(articulo.autor)

    for letra in letras:
        for autor in autores_unicos:
            if autor.split()[-1][0].upper() == letra:
                if letra not in autores_por_letra.keys():
                    autores_por_letra[letra] = []
                    autores_por_letra[letra].append(autor)
                else:
                    autores_por_letra[letra].append(autor)

    return autores_por_letra