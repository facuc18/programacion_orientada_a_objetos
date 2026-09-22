from strategy.estrategia import EstrategiaPrecio
from strategy.resultado import ResultadoEstrategia
from models.compra import Compra


class DescuentoBlackFriday(EstrategiaPrecio):
    """
    Estrategia agregada para el desafío.

    No modifica ninguna estrategia existente.
    """

    PORCENTAJE = 0.10

    def aplicar(
        self,
        compra: Compra,
        precio_actual: float,
    ) -> ResultadoEstrategia:

        monto = precio_actual * self.PORCENTAJE
        precio_resultante = precio_actual - monto

        return ResultadoEstrategia(
            "Black Friday",
            -monto,
            precio_resultante,
        )
