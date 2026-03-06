import subprocess
import sys
from sistema_acoplado.acoplado import crear_orden_acoplada

VERDE   = "\033[92m"
ROJO    = "\033[91m"
AMARILLO= "\033[93m"
CYAN    = "\033[96m"
NEGRITA = "\033[1m"
RESET   = "\033[0m"

def ok(txt):    print(f"  {VERDE} {txt}{RESET}")
def error(txt): print(f"  {ROJO} {txt}{RESET}")
def info(txt):  print(f"  {CYAN} {txt}{RESET}")
def warn(txt):  print(f"  {AMARILLO} {txt}{RESET}")
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
        warn("Monto inválido, se usará 5.000.000.")
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
    titulo("OPCIÓN 1 — Acoplamiento directo con PSE")

    cliente, monto = pedir_datos()

    print(f"  {NEGRITA}Llamada al proveedor:{RESET}")
    try:
        orden = crear_orden_acoplada(cliente, monto)
        mostrar_orden(orden)
    except Exception as e:
        error(f"Error inesperado: {e}")


def menu():
    while True:
        titulo("TALLER II — INTEROPERABILIDAD ADAPTADOR DE INTERFAZ" )
        print(f"  {NEGRITA}1.{RESET} Implementacion Ingenuea Acoplamiento — PSE")
        print()
        opcion = input("  Selecciona una opción: ").strip()

        if   opcion == "1": opcion_1()
        elif opcion == "0":
            print()
            info("Hasta luego.")
            break
        else:
            warn("Opción no válida.")

        print()
        input("Presiona Enter para volver al menú")


if __name__ == "__main__":
    menu()