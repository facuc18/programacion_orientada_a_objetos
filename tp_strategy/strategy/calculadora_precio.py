from models.compra import Compra
from strategy.estrategia import EstrategiaPrecio


class CalculadoraPrecio:
    """
    Contexto de Strategy.

    Mantiene una colección de estrategias y las ejecuta en orden.
    """

    def __init__(self):
        self.estrategias: list[EstrategiaPrecio] = []

    def agregar_estrategia(self, estrategia: EstrategiaPrecio):
        """Permite agregar una nueva estrategia sin modificar las existentes."""
        self.estrategias.append(estrategia)

    def calcular(self, compra: Compra) -> float:
        precio_actual = compra.subtotal

        print(f"Precio inicial: ${precio_actual:.2f}")

        for estrategia in self.estrategias:
            resultado = estrategia.aplicar(compra, precio_actual)

            signo = "+" if resultado.monto >= 0 else "-"
            monto = abs(resultado.monto)

            print(
                f"[Strategy] {resultado.nombre}: "
                f"{signo}${monto:.2f} → ${resultado.precio_resultante:.2f}"
            )

            precio_actual = resultado.precio_resultante

        print(f"Precio final: ${precio_actual:.2f}")

        return precio_actual
