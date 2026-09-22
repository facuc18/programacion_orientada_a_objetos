class ResultadoEstrategia:
    """Guarda la información producida por una estrategia."""

    def __init__(self, nombre: str, monto: float, precio_resultante: float):
        self.nombre = nombre
        self.monto = monto
        self.precio_resultante = precio_resultante
