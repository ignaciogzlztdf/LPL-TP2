from clases.excepciones import LongitudInvalidaError

class Articulo:
    def __init__(self, titulo, autor, texto):
        self._validar_longitud("título", titulo)
        self._validar_longitud("texto",texto)
        self._titulo = titulo
        self._autor = autor
        self._texto = texto

    def _validar_longitud(self, nombre_atributo, valor):
        if len(valor.strip()) < 10:
            raise LongitudInvalidaError(nombre_atributo, valor)

    def to_html(self):
        return f"""<article>
                                <h2>{self.titulo}</h2>
                                <h5>{self.autor}</h5>
                                <p>{self.texto[:300] + ("…" if len(self.texto) > 300 else "")}</p>
                            </article>"""

    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
    @property
    def autor(self):
        return self._autor
    @autor.setter
    def autor(self, autor):
        self._autor = autor
    @property
    def texto(self):
        return self._texto
    @texto.setter
    def texto(self, texto):
        self._texto = texto