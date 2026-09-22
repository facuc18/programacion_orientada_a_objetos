from chain.handler import Handler
from models.pedido import Pedido


class ValidarCliente(Handler):

    def validar(self, pedido: Pedido) -> bool:
        if pedido.cliente_valido:
            print("Validar Cliente → OK")
            return True

        pedido.motivo_rechazo = "Cliente inválido."
        print(f" Validar Cliente → ERROR: {pedido.motivo_rechazo}")
        return False
