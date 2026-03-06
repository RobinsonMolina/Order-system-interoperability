# main.py

from sistema_acoplado.acoplado import crear_orden_acoplada, orden_acoplada_paypal

VERDE    = "\033[92m"
ROJO     = "\033[91m"
NEGRITA  = "\033[1m"
RESET    = "\033[0m"

def ok(txt):        print(f"  {VERDE} {txt}{RESET}")
def error(txt):     print(f"  {ROJO} {txt}{RESET}")
def linea(c="─", n=58): print(c * n)
def titulo(t):
    print(); linea("═"); print(f"  {NEGRITA}{t}{RESET}"); linea("═")


def pedir_datos():
    print()
    cliente = input(f"  {NEGRITA}Cliente ID {RESET}(Enter = 'cliente-001'): ").strip() or "cliente-001"
    monto_s = input(f"  {NEGRITA}Monto COP  {RESET}(Enter = 5000000)     : ").strip() or "5000000"
    try:
        monto = float(monto_s)
    except ValueError:
        print("Monto inválido, se usará 5.000.000.")
        monto = 5_000_000.0
    return cliente, monto


def mostrar_orden(orden):
    print()
    aprobado = orden["estado"] == "APROBADO"
    if aprobado:
        ok(f"Pago {orden['estado']}")
    else:
        error(f"Pago {orden['estado']}")
    print(f"  Orden ID            : {orden['ordenId']}")
    print(f"  Código autorización : {orden.get('codigoAutorizacion') or '—'}")


def opcion_1():
    titulo("PASO 1 — Acoplamiento directo con PSE")

    cliente, monto = pedir_datos()

    print(f"\n  {NEGRITA}Llamada al proveedor:{RESET}")
    try:
        orden = crear_orden_acoplada(cliente, monto)
        mostrar_orden(orden)
    except Exception as e:
        error(f"Error inesperado: {e}")


def opcion_2():
    titulo("PASO 2 — Análisis de impacto del cambio (PayPal)")

    cliente, monto = pedir_datos()

    print(f"\n  {NEGRITA}Llamada al proveedor:{RESET}")
    try:
        orden = orden_acoplada_paypal(cliente, monto)
        mostrar_orden(orden)
    except TypeError as e:
        error(f"TypeError → {e}")
        print()
        print(f"  {ROJO}Causa: PayPal exige 'descripcion' y 'producto' pero el sistema no lo envía.{RESET}")
        print(f"  {ROJO}Para corregirlo habría que modificar el sistema principal.{RESET}")
    except KeyError as e:
        error(f"KeyError → campo {e} ya no existe en la respuesta de PayPal")
        print()
        print(f"  {ROJO}Causa: el campo fue renombrado por PayPal.{RESET}")
        print(f"  {ROJO}El sistema principal debe actualizarse.{RESET}")


def menu():
    while True:
        titulo("TALLER II — INTEROPERABILIDAD ADAPTADOR DE INTERFAZ")
        print(f"  {NEGRITA}1.{RESET} Paso 1 — Implementación ingenua acoplada (PSE)")
        print(f"  {NEGRITA}2.{RESET} Paso 2 — Análisis de impacto del cambio (PayPal)")
        print(f"  {NEGRITA}0.{RESET} Salir")
        print()
        opcion = input("  Selecciona una opción: ").strip()

        if   opcion == "1": opcion_1()
        elif opcion == "2": opcion_2()
        elif opcion == "0":
            print()
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")

        print()
        input("  Presiona Enter para volver al menú...")


if __name__ == "__main__":
    menu()