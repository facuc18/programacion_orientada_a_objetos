class Compra:
    """Representa los datos necesarios para calcular el precio de una compra."""

    def __init__(
        self,
        subtotal: float,
        cliente_tipo: str,
        cantidad_productos: int,
        tipo_envio: str,
    ):
        self.subtotal = subtotal
        self.cliente_tipo = cliente_tipo
        self.cantidad_productos = cantidad_productos
        self.tipo_envio = tipo_envio
