from interfaz.servicioPago import ServicioPago

class SistemaOrdenes:

    def __init__(self, servicio_pago: ServicioPago):
        self._servicio = servicio_pago

    def crearOrden(self, cliente_id: str, monto: float) -> dict:
    
        resultado = self._servicio.procesarPago(cliente_id, monto)

        return {
            "ordenId":            f"ORD-{cliente_id}-001",
            "estado":             resultado["estado"],
            "codigoAutorizacion": resultado["codigoAutorizacion"]
        }