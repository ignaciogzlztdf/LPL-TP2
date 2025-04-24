class LongitudInvalidaError(Exception):
    """Excepción lanzada cuando el título o texto son demasiado cortos.""" # Para tenerlo en __doc__
    def __init__(self, nombre_atributo, valor, longitud_minima=10):
        super().__init__(
            f"""
            El campo '{nombre_atributo}' debe tener al menos {longitud_minima} caracteres.
            Longitud actual: {len(valor)}."""
        )
        self.nombre_atributo = nombre_atributo
        self.valor = valor
        self.longitud_minima = longitud_minima