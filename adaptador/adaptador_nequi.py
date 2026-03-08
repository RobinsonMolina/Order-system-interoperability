from interfaz.servicioPago import ServicioPago
from proveedor.proveedor_externo_nequi import Nequi

class AdaptadorNequi(ServicioPago):
    """
    Adapta Nequi (interfaz totalmente diferente) al contrato interno.
    El sistema principal lo usa exactamente igual que los adaptadores PSE y Paypal.
    """

    def __init__(self):
        self._proveedor = Nequi()

    def procesarPago(self, clienteId: str, monto: float) -> dict:
        r = self._proveedor.submit_payment(
            account_ref=clienteId,
            value=monto,
            iso_currency="COP"
        )
        return {
            "estado":             "APROBADO" if r["success"] else "RECHAZADO",
            "codigoAutorizacion": r["confirmation_code"]
        }