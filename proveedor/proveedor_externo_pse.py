
# Proveedor externo - PSE

from datetime import datetime, timezone

class PSE:

    #respuesta del proveedor
    CODIGO_APROBADO  = "00"
    CODIGO_RECHAZADO = "51"
    LIMITE_MONTO = 10_000_000

    def executeTransaction(self, user: str,amount: float,currency: str) -> dict:
        print(
            f"  [PSE] executeTransaction("
            f"user='{user}', amount={amount:,.0f}, currency='{currency}')"
        )

        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

        if amount <= self.LIMITE_MONTO:
            return {
                "resultCode": self.CODIGO_APROBADO,
                "authId":     "PSE-AUTH-4471",
                "timestamp":  timestamp
            }

        return {
            "resultCode": self.CODIGO_RECHAZADO,
            "authId":     None,
            "timestamp":  timestamp
        }