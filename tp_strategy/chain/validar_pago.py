from chain.handler import Handler
from models.pedido import Pedido


class ValidarPago(Handler):

    def validar(self, pedido: Pedido) -> bool:
        if pedido.pago_aprobado:
            print("[Chain] Validar Pago → OK")
            return True

        pedido.motivo_rechazo = "El pago fue rechazado."
        print(f"[Chain] Validar Pago → ERROR: {pedido.motivo_rechazo}")
        return False
