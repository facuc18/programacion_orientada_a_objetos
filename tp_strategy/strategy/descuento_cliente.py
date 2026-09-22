from strategy.estrategia import EstrategiaPrecio
from strategy.resultado import ResultadoEstrategia
from models.compra import Compra


class DescuentoCliente(EstrategiaPrecio):
    """Aplica descuento según el tipo de cliente."""

    DESCUENTOS = {
        "comun": 0.00,
        "premium": 0.10,
        "vip": 0.15,
    }

    def aplicar(
        self,
        compra: Compra,
        precio_actual: float,
    ) -> ResultadoEstrategia:

        descuento = self.DESCUENTOS.get(compra.cliente_tipo.lower(), 0.00)

        monto = precio_actual * descuento
        precio_resultante = precio_actual - monto

        nombre = f"Descuento cliente {compra.cliente_tipo}"

        return ResultadoEstrategia(
            nombre,
            -monto,
            precio_resultante,
        )
