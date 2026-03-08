from interfaz.servicioPago import ServicioPago
from proveedor.proveedor_externo_pse import PSE
class AdaptadorPSE(ServicioPago):
    """Adapta PSE al contrato interno."""

    def __init__(self):
        self._proveedor = PSE()

    def procesarPago(self, clienteId: str, monto: float) -> dict:
        # Traduce parámetros internos → formato PSE
        r = self._proveedor.executeTransaction(
            user=clienteId,
            amount=monto,
            currency="COP"
        )
        # Traduce respuesta PSE → contrato interno
        return {
            "estado":              "APROBADO" if r["resultCode"] == "00" else "RECHAZADO",
            "codigoAutorizacion":  r["authId"]
        }