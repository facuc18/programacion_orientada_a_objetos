from abc import ABC, abstractmethod

from models.pedido import Pedido


class Handler(ABC):
    """
    Handler abstracto de Chain of Responsibility.

    Cada handler puede validar algo y decidir si continúa
    con el siguiente o detiene el procesamiento.
    """

    def __init__(self):
        self.siguiente = None

    def set_siguiente(self, siguiente: "Handler") -> "Handler":
        self.siguiente = siguiente
        return siguiente

    def manejar(self, pedido: Pedido) -> bool:
        """
        Ejecuta la validación actual.

        Si es correcta, pasa al siguiente.
        Si falla, detiene la cadena.
        """
        if not self.validar(pedido):
            return False

        if self.siguiente is not None:
            return self.siguiente.manejar(pedido)

        pedido.aprobado = True
        return True

    @abstractmethod
    def validar(self, pedido: Pedido) -> bool:
        pass

    def nombre(self) -> str:
        return self.__class__.__name__
