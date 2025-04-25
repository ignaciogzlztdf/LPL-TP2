import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from clases.articulo import Articulo

# Test para Articulo.to_html()
def test_to_html():
    art = Articulo("Título Prueba", "Autor Prueba", "Texto del artículo")
    html = art.to_html()
    print(html)
    assert 'Título Prueba' in html
    assert "<h5>Autor Prueba</h5>" in html
    assert "<p>Texto del artículo</p>" in html
    print("test_to_html pasó")

test_to_html()