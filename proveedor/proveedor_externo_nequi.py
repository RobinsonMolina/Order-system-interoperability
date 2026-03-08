class Nequi:
    
    LIMITE_MONTO = 10_000_000
    CODIGO_APROBADO  = True
    CODIGO_RECHAZADO = False
    

    def submit_payment(self, account_ref: str,
                       value: float, iso_currency: str) -> dict:
        print(f"    → [Nequi] submit_payment("
              f"account_ref='{account_ref}', value={value}, "
              f"iso_currency='{iso_currency}')")

        if value <= self.LIMITE_MONTO:
            return {
                "success":           self.CODIGO_APROBADO,
                "confirmation_code": "NQI-7731-OK",
                "error_msg":         None
            }
        else:
            return {
                "success":           self.CODIGO_RECHAZADO,
                "confirmation_code": None,
                "error_msg":         "Saldo insuficiente"
            }