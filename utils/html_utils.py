from clases.articulo import Articulo
from datetime import datetime

def generar_footer():
    # Genero la fecha actual en un formato legible
    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")

    # Genero el footer con la fecha de generación
    return f"""
    <footer>
        <p>Fecha y hora de generación: {fecha_actual}</p>
    </footer>
    """


def generar_html_articulo(articulo:Articulo, articulo_anterior=None, articulo_siguiente=None):
    enlaces_navegacion = "<div class='d-flex justify-content-between'>"

    if articulo_anterior:
        enlace_anterior = articulo_anterior.titulo.replace(" ", "_").lower() + ".html"
        enlaces_navegacion += f'<a href="{enlace_anterior}">&larr; Anterior</a>'
    else:
        enlaces_navegacion += "<span></span>"

    if articulo_siguiente:
        enlace_siguiente = articulo_siguiente.titulo.replace(" ", "_").lower() + ".html"
        enlaces_navegacion += f'<a href="{enlace_siguiente}">Siguiente &rarr;</a>'
    else:
        enlaces_navegacion += "<span></span>"

    enlaces_navegacion += "</div><hr>"

    # Generar HTML para el artículo específico
    html_articulo = f"""
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
            <h1>Artículo</h1>
            <hr>
        </header>
        {articulo.to_html_sin_link()}
        {enlaces_navegacion}
        <hr>
        <a href="../index.html">Volver a la página principal</a>
        {generar_footer()}
    </body>
    </html>
    """
    return html_articulo.strip()


def generar_tabla_html_articulos_por_autor(articulos_por_autor):
    html = """
    <table border="1" style="border-collapse: collapse; width: 50%;">
        <thead>
            <tr>
                <th>Autor</th>
                <th>Cantidad de artículos</th>
            </tr>
        </thead>
        <tbody>
    """
    for autor, cantidad in articulos_por_autor.items():
        html += f"""
            <tr>
                <td>{autor}</td>
                <td>{cantidad}</td>
            </tr>
        """
    html += """
        </tbody>
    </table>
    """
    return html

def generar_tabla_html_autores_por_letra(autores_por_letra):
    html = """
    <table border="1" style="border-collapse: collapse; width: 50%;">
        <thead>
            <tr>
                <th>Letra</th>
                <th>Autores</th>
            </tr>
        </thead>
        <tbody>
    """
    for letra, lista_autores in autores_por_letra.items():
        if not lista_autores:
             html += f"""
            <tr>
                <td>{letra}</td>
                <td> - </td>
            </tr>
        """
        else:
            lista_autores = ", ".join(sorted(lista_autores))
            html += f"""
                <tr>
                    <td>{letra}</td>
                    <td>{lista_autores}</td>
                </tr>
            """
    html += """
        </tbody>
    </table>
    """
    return html