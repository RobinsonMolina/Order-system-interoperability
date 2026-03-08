import unittest
from interfaz.servicioPago import ServicioPago
from adaptador.adaptador_pse import AdaptadorPSE
from adaptador.adaptador_paypal import AdaptadorPaypal
from adaptador.adaptador_nequi import AdaptadorNequi
from sistema_orden.sistemaConInterfaz import SistemaOrdenes

print("""
============================================================================================================================================================================
                                                                             EJECUTANDO TESTS
============================================================================================================================================================================
""")

class TestAdaptadores(unittest.TestCase):
    """Pruebas básicas para asegurar que los adaptadores funcionen"""

    def test_pse_aprobado(self):
        # El sistema debe recibir 'APROBADO' desde el adaptador PSE
        r = AdaptadorPSE().procesarPago("usuario-1", 5000)
        self.assertEqual(r["estado"], "APROBADO")

    def test_paypal_aprobado(self):
        # El sistema debe recibir 'APROBADO' desde el adaptador Paypal
        r = AdaptadorPaypal().procesarPago("usuario-2", 5000)
        self.assertEqual(r["estado"], "APROBADO")
        # Paypal devuelve 'autorizacion',pero el sistema espera 'codigoAutorizacion'. Verifica que se traduzca.
        self.assertNotIn("autorizacion", r)
        
    def test_nequi_aprobado(self):
        # El sistema debe recibir 'APROBADO' desde el adaptador Nequi
        r = AdaptadorNequi().procesarPago("usuario-3", 5000)
        self.assertEqual(r["estado"], "APROBADO")

class TestIntercambiabilidad(unittest.TestCase):
    """El sistema de órdenes funciona con cualquier proveedor"""

    def test_sistema_con_pse(self):
        sistema = SistemaOrdenes(AdaptadorPSE())
        orden = sistema.crearOrden("cliente-1", 1000)
        self.assertEqual(orden["estado"], "APROBADO")

    def test_sistema_con_paypal(self):
        sistema = SistemaOrdenes(AdaptadorPaypal())
        orden = sistema.crearOrden("cliente-2", 1000)
        self.assertEqual(orden["estado"], "APROBADO")

    def test_sistema_con_nequi(self):
        sistema = SistemaOrdenes(AdaptadorNequi())
        orden = sistema.crearOrden("cliente-3", 1000)
        self.assertEqual(orden["estado"], "APROBADO")

if __name__ == "__main__":
    unittest.main(verbosity=1)