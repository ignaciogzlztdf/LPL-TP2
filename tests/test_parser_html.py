import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from clases.articulo import Articulo
from clases.parser_html import ParserHtml

# Test para ParserHtml.filtrar_articulos()
def test_filtrar_articulos_invalidos():
    try:
        parser = ParserHtml([])
    except ValueError as e:
        assert str(e) == "No hay artículos válidos para procesar."
        print("test_filtrar_articulos pasó (capturó el error esperado)")
    else:
        assert False, "No lanzó ValueError con artículo inválido"

test_filtrar_articulos_invalidos()