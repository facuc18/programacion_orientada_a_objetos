from strategy.estrategia import EstrategiaPrecio
from strategy.resultado import ResultadoEstrategia
from models.compra import Compra


class DescuentoCantidad(EstrategiaPrecio):
    """Aplica descuento según la cantidad de productos."""

    def aplicar(
        self,
        compra: Compra,
        precio_actual: float,
    ) -> ResultadoEstrategia:

        if compra.cantidad_productos > 10:
            porcentaje = 0.10
        elif compra.cantidad_productos > 5:
            porcentaje = 0.05
        else:
            porcentaje = 0.00

        monto = precio_actual * porcentaje
        precio_resultante = precio_actual - monto

        nombre = "Descuento por cantidad"

        return ResultadoEstrategia(
            nombre,
            -monto,
            precio_resultante,
        )
