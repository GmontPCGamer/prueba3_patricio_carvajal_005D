import csv, msvcrt, os

def menu():
    print("MENU DE OPCIONES:")
    print("1) Registrar pedido")
    print("2) Listar todos los pedidos.")
    print("3) Buscar pedido por RUT.")
    print("4) Imprimir hoja de ruta.")
    print("5) Salir del programa.")

    opc = int(input('\nIngrese opción: '))

    return opc