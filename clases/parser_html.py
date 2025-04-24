from clases.articulo import Articulo
from datetime import datetime
from collections import defaultdict
from utils.files_utils import guardar_en_archivo_html, crear_carpeta_html_articulos
from utils.html_utils import generar_html_articulo
import os

class ParserHtml:
    def __init__(self, articulos):
        articulos_filtrados = self.filtrar_articulos(articulos)
        if not articulos_filtrados:
            raise ValueError("No hay artículos válidos para procesar.")
        
        self.articulos = articulos_filtrados

        # Crear carpeta para guardar los archivos HTML de los artículos
        crear_carpeta_html_articulos()
        # Generar HTML para cada artículo y guardarlo en un archivo
        for articulo in self.articulos:
            self.crear_archivo_html_articulo(generar_html_articulo(articulo), articulo.titulo.replace(' ', '_').lower())


    def filtrar_articulos(self, articulos):
        articulos_filtrados = []

        for articulo in articulos:
            if not isinstance(articulo, Articulo):
                raise ValueError("Cada artículo debe ser una instancia de Articulo.")
            
            titulo = articulo.titulo
            autor = articulo.autor
            texto = articulo.texto
            
            if not isinstance(titulo, str) or not isinstance(autor, str) or not isinstance(texto, str):
                raise ValueError("El título, autor y texto deben ser cadenas.")

            if not titulo.strip() or not autor.strip() or not texto.strip():
                raise ValueError("El nombre, autor y texto no pueden estar vacíos.")

            articulos_filtrados.append(articulo)

        return articulos_filtrados


    def generar_html_principal(self):
        # Agrupar artículos por autor
        autores = defaultdict(list)
        for articulo in self.articulos:
            autores[articulo.autor].append(articulo)

        # Ordenar autores alfabéticamente
        autores = dict(sorted(autores.items()))
        # Ordenar artículos por título dentro de cada autor
        for autor in autores:
            autores[autor] = sorted(autores[autor], key=lambda x: x.titulo)

        # Meto la info de cada artículo en una estructura HTML
        articulos_html = ""
        for autor, articulos_autor in autores.items():
            articulos_html += f"""
            <section id="{autor.replace(' ', '_').lower()}">
                <div class="container">
                    <h3>Artículos de {autor}</h3>
                    <div class="row">"""
            for articulo in articulos_autor:
                articulos_html += f"""
                        <div class="col-sm-4">
                            {articulo.to_html()}
                        </div>"""
            articulos_html += """
                    </div>
                </div>
            </section>\n"""

        # Genero la fecha actual en un formato legible
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Genero el índice de autores
        indice_html = """<h2>Índice de Autores</h2>
                <ul>"""
        for autor in autores.keys():
            indice_html += f"""
                    <li><a href="#{autor.replace(" ", "_").lower()}">{autor}</a></li>"""
        indice_html += """
                </ul>"""

        # Genero el HTML y le agrego: artículos y fecha actual
        html = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Artículos</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
            <style>
                body {{ font-family: Arial, sans-serif; }}
                header {{ text-align: center; }}
                article {{ margin: 20px; padding: 10px; border: 1px solid #ccc; }}
                footer {{ text-align: center; margin-top: 20px; }}
                h1 {{ color: #333; }}
                h2 {{ color: #555; }}
                h4 {{ color: #777; }}
                p {{ color: #999; }}
                hr {{ border: 1px solid #ccc; }}
            </style>
        </head>
        <body>
            <header>
                <h1>Mi Sitio de Artículos</h1>
                <hr>
            </header>
            <nav>
                {indice_html}
            </nav>
            {articulos_html}
            <footer>
                <p>Fecha de generación: {fecha_actual}</p>
            </footer>
        </body>
        </html>
        """
        return html.strip()


    def crear_archivo_html_principal(self, html_principal:str):
        html_principal = self.generar_html_principal()
        # Guardo el HTML en un archivo
        archivo_nombre = "index.html"

        guardar_en_archivo_html(archivo_nombre, html_principal)


    def crear_archivo_html_articulo(self, html_articulo:str, nombre_archivo:str, carpeta_html_articulos="html_articulos"):
        # Construyo la ruta completa
        ruta_completa = os.path.join(carpeta_html_articulos, f"{nombre_archivo}.html")
        # Guardo el HTML en un archivo
        guardar_en_archivo_html(ruta_completa, html_articulo)