from models.compra import Compra
from models.pedido import Pedido

from strategy.calculadora_precio import CalculadoraPrecio
from strategy.descuento_cliente import DescuentoCliente
from strategy.descuento_cantidad import DescuentoCantidad
from strategy.descuento_black_friday import DescuentoBlackFriday
from strategy.envio import Envio

from chain.validar_cliente import ValidarCliente
from chain.validar_stock import ValidarStock
from chain.validar_pago import ValidarPago
from chain.validar_limite_compra import ValidarLimiteCompra


def crear_calculadora() -> CalculadoraPrecio:
    """
    Construye la colección de estrategias.

    Para agregar una nueva regla, simplemente se puede crear
    otra clase que implemente EstrategiaPrecio y agregarla aquí.
    """
    calculadora = CalculadoraPrecio()

    calculadora.agregar_estrategia(DescuentoCliente())
    calculadora.agregar_estrategia(DescuentoCantidad())
    calculadora.agregar_estrategia(DescuentoBlackFriday())
    calculadora.agregar_estrategia(Envio())

    return calculadora


def crear_cadena() -> ValidarCliente:
    """
    Construye la Chain of Responsibility.

    El orden es:
    Cliente → Stock → Pago → Límite de compra
    """
    cliente = ValidarCliente()
    stock = ValidarStock()
    pago = ValidarPago()
    limite = ValidarLimiteCompra()

    cliente.set_siguiente(stock).set_siguiente(pago).set_siguiente(limite)

    return cliente


def procesar_pedido(numero: int, pedido: Pedido):
    print("\n" + "=" * 60)
    print(f"PEDIDO {numero}")
    print("=" * 60)

    print("\n--- Cálculo del precio ---")

    calculadora = crear_calculadora()
    pedido.precio_final = calculadora.calcular(pedido.compra)

    print("\n--- Cadena de validación ---")

    cadena = crear_cadena()
    resultado = cadena.manejar(pedido)

    if resultado:
        print("\nRESULTADO: PEDIDO APROBADO")
    else:
        print("\nRESULTADO: PEDIDO RECHAZADO")
        print(f"MOTIVO: {pedido.motivo_rechazo}")


def main():
    # ---------------------------------------------------------
    # PEDIDO 1: aprobado
    # ---------------------------------------------------------
    compra_aprobada = Compra(
        subtotal=100_000,
        cliente_tipo="vip",
        cantidad_productos=12,
        tipo_envio="express",
    )

    pedido_aprobado = Pedido(
        compra=compra_aprobada,
        cliente_valido=True,
        stock_disponible=True,
        pago_aprobado=True,
    )

    procesar_pedido(1, pedido_aprobado)

    # ---------------------------------------------------------
    # PEDIDO 2: rechazado por falta de stock
    # ---------------------------------------------------------
    compra_sin_stock = Compra(
        subtotal=80_000,
        cliente_tipo="premium",
        cantidad_productos=8,
        tipo_envio="normal",
    )

    pedido_sin_stock = Pedido(
        compra=compra_sin_stock,
        cliente_valido=True,
        stock_disponible=False,
        pago_aprobado=True,
    )

    procesar_pedido(2, pedido_sin_stock)

    # ---------------------------------------------------------
    # PEDIDO 3: rechazado por problema de pago
    # ---------------------------------------------------------
    compra_pago_rechazado = Compra(
        subtotal=120_000,
        cliente_tipo="vip",
        cantidad_productos=6,
        tipo_envio="normal",
    )

    pedido_pago_rechazado = Pedido(
        compra=compra_pago_rechazado,
        cliente_valido=True,
        stock_disponible=True,
        pago_aprobado=False,
    )

    procesar_pedido(3, pedido_pago_rechazado)

    # ---------------------------------------------------------
    # PEDIDO 4: rechazado por límite de compra
    # ---------------------------------------------------------
    compra_supera_limite = Compra(
        subtotal=700_000,
        cliente_tipo="comun",
        cantidad_productos=1,
        tipo_envio="sucursal",
    )

    pedido_supera_limite = Pedido(
        compra=compra_supera_limite,
        cliente_valido=True,
        stock_disponible=True,
        pago_aprobado=True,
    )

    procesar_pedido(4, pedido_supera_limite)


if __name__ == "__main__":
    main()
