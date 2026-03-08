import subprocess
import sys
from sistema_orden.acoplado import crear_orden_acoplada_pse, crear_orden_acoplada_paypal
from adaptador.adaptador_pse import AdaptadorPSE
from adaptador.adaptador_paypal import AdaptadorPaypal
from adaptador.adaptador_nequi import AdaptadorNequi
from sistema_orden.sistemaConInterfaz import SistemaOrdenes

def mostrar_orden(orden):
    print("\n  --- Resultado de la Transacción ---")
    print(f"  Estado              : {orden['estado']}")
    print(f"  Orden ID            : {orden['ordenId']}")
    print(f"  Código Autorización : {orden.get('codigoAutorizacion') or 'N/A'}\n")

def pedir_datos():
    cliente = input("\n  Cliente ID (Enter = 'cli-001'): ").strip() or "cli-001"
    monto_s = input("  Monto COP  (Enter = 50000)  : ").strip() or "50000"
    return cliente, float(monto_s) if monto_s.isdigit() else 50000.0

def menu():
    while True:
        print("\n=== INTEROPERABILIDAD DE PAGOS ===")
        print("  1. Acoplamiento directo - PSE (Funciona)")
        print("  2. Acoplamiento directo - Paypal (Falla por acoplamiento)")
        print("  3. Sistema con Adaptador (Estable)")
        print("  4. Ejecutar Pruebas")
        print("  0. Salir")
        
        opc = input("\n  Selecciona una opción: ").strip()

        if opc == "0": break

        if opc in ["1", "2"]:
            cliente, monto = pedir_datos()
            try:
                if opc == "1":
                    orden = crear_orden_acoplada_pse(cliente, monto)
                else:
                    orden = crear_orden_acoplada_paypal(cliente, monto)
                mostrar_orden(orden)
            except Exception as e:
                print(f"\n  [ERROR] Fallo de integración: {e}")
                print("  El sistema falló al intentar usar un proveedor distinto de la forma acoplada.")
        
        elif opc == "3":
            print("\n  a) PSE\n  b) Paypal\n  c) Nequi")
            sel = input("  Elige proveedor: ").strip().lower()
            
            adps = {"a": AdaptadorPSE(), "b": AdaptadorPaypal(), "c": AdaptadorNequi()}
            adaptador = adps.get(sel, AdaptadorPSE())
            
            cliente, monto = pedir_datos()
            orden = SistemaOrdenes(adaptador).crearOrden(cliente, monto)
            mostrar_orden(orden)
            
        elif opc == "4":
            print("\n  Ejecutando pruebas...")
            resultado = subprocess.run(

            [sys.executable, "-m", "unittest", "discover", "tests", "-v"],
                capture_output=False

            )

            print()

            if resultado.returncode == 0:

                print("Todas las pruebas pasaron correctamente.")

            else:

                print("Algunas pruebas fallaron. Revisa la salida anterior.")
        
        else:
            print("  Opción no válida.")

if __name__ == "__main__":
    menu()