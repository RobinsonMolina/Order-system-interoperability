
# Proveedor externo con cambios para el paso 2 - PayPal
class Paypal:
    
    #respuesta del proveedor
    CODIGO_APROBADO  = "APROBADO"
    CODIGO_RECHAZADO = "RECHAZADO"
    LIMITE_MONTO = 10_000_000

    def executeTransaction(self, user: str,amount: float,currency: str, descripcion: str, producto: int ) -> dict: #LA DESCRIPCION SE DA COMO NUEVO PARAMETRO
        print(
            f"  [PayPal] executeTransaction("
            f"user='{user}', amount={amount:,.0f}, currency='{currency}, descripcion='{descripcion}', producto='{producto}')"
        )

        if amount <= self.LIMITE_MONTO:
            return {
                "estado": self.CODIGO_APROBADO,
                "autorizacion": "PAYPAL-AUTH-4567"
            }

        return {
            "estado": self.CODIGO_RECHAZADO,
            "autorizacion":     None
        }