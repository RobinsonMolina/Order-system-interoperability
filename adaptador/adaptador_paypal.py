from interfaz.servicioPago import ServicioPago
from proveedor.proveedor_externo_paypal import Paypal

class AdaptadorPaypal(ServicioPago):
    """Adapta Paypal al contrato interno."""
    def __init__(self, descripcion: str = "Pago Orden", producto: int = 1):
        self._proveedor = Paypal()
        self._descripcion = descripcion
        self._producto = producto

    def procesarPago(self, clienteId: str, monto: float) -> dict:
        # Traduce parámetros internos → formato Paypal
        r = self._proveedor.executeTransaction(
            user=clienteId,
            amount=monto,
            currency="COP",
            descripcion=self._descripcion,
            producto=self._producto
        )
        # Traduce respuesta Paypal → contrato interno (campos renombrados)
        return {
            "estado": r["estado"],
            "codigoAutorizacion": r["autorizacion"]
        }