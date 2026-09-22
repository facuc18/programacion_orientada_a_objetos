from abc import ABC, abstractmethod

from models.compra import Compra
from strategy.resultado import ResultadoEstrategia


class EstrategiaPrecio(ABC):
    """
    Interfaz/base abstracta de Strategy.

    Cada regla de precio debe implementar aplicar().
    """

    @abstractmethod
    def aplicar(
        self,
        compra: Compra,
        precio_actual: float,
    ) -> ResultadoEstrategia:
        pass
