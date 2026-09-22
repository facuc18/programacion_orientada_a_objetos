from chain.handler import Handler
from models.pedido import Pedido


class ValidarStock(Handler):

    def validar(self, pedido: Pedido) -> bool:
        if pedido.stock_disponible:
            print(" Validar Stock → OK")
            return True

        pedido.motivo_rechazo = "Stock insuficiente."
        print(f"Validar Stock → ERROR: {pedido.motivo_rechazo}")
        return False
