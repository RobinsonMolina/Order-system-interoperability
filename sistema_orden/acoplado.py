from proveedor.proveedor_externo_pse import PSE
from proveedor.proveedor_externo_paypal import Paypal

class SistemaOrdenesAcoplado:
    
    CODIGO_APROBADO = "00"

    def __init__(self, proveedor):
        self._proveedor = proveedor

    def crearOrden(self, cliente_id: str, monto: float) -> dict:
        respuesta = self._proveedor.executeTransaction(
            user=cliente_id,
            amount=monto,
            currency="COP"
        )

        aprobado = respuesta["resultCode"] == self.CODIGO_APROBADO

        return {
            "ordenId":            f"ORD-{cliente_id}-001",
            "estado":             "APROBADO" if aprobado else "RECHAZADO",
            "codigoAutorizacion": respuesta["authId"]
        }

#crear una orden usando el sistema acoplado
def crear_orden_acoplada_pse(cliente_id: str, monto: float) -> dict:
    return SistemaOrdenesAcoplado(PSE()).crearOrden(cliente_id, monto)

#crear una orden con cambios en el proveedor
def crear_orden_acoplada_paypal(cliente_id: str, monto: float) -> dict:
     return SistemaOrdenesAcoplado(Paypal()).crearOrden(cliente_id, monto)