from abc import ABC, abstractmethod

class ServicioPago(ABC):

    @abstractmethod
    def procesarPago(self, clienteId: str, monto: float) -> dict:
        pass
