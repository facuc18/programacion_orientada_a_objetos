from strategy.estrategia import EstrategiaPrecio
from strategy.resultado import ResultadoEstrategia
from models.compra import Compra


class Envio(EstrategiaPrecio):
    """Agrega el costo correspondiente al tipo de envío."""

    COSTOS = {
        "sucursal": 0.0,
        "normal": 5000.0,
        "express": 10000.0,
    }

    def aplicar(
        self,
        compra: Compra,
        precio_actual: float,
    ) -> ResultadoEstrategia:

        costo = self.COSTOS.get(compra.tipo_envio.lower(), 0.0)
        precio_resultante = precio_actual + costo

        return ResultadoEstrategia(
            f"Envío {compra.tipo_envio}",
            costo,
            precio_resultante,
        )
