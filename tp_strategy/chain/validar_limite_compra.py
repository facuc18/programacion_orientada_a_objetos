from chain.handler import Handler
from models.pedido import Pedido


class ValidarLimiteCompra(Handler):
    """
    Validador agregado para el desafío.

    No modifica los handlers anteriores.
    """

    LIMITE = 500_000.0

    def validar(self, pedido: Pedido) -> bool:
        if pedido.precio_final <= self.LIMITE:
            print("Validar Límite de Compra → OK")
            return True

        pedido.motivo_rechazo = (
            f"El precio final supera el límite de "
            f"${self.LIMITE:.2f}."
        )
        print(
            " Validar Límite de Compra → "
            f"ERROR: {pedido.motivo_rechazo}"
        )
        return False
