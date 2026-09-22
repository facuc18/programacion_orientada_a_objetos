from models.compra import Compra


class Pedido:
    """Representa un pedido que será validado por la cadena."""

    def __init__(
        self,
        compra: Compra,
        cliente_valido: bool = True,
        stock_disponible: bool = True,
        pago_aprobado: bool = True,
    ):
        self.compra = compra
        self.cliente_valido = cliente_valido
        self.stock_disponible = stock_disponible
        self.pago_aprobado = pago_aprobado

        self.precio_final = 0.0
        self.aprobado = False
        self.motivo_rechazo = None
