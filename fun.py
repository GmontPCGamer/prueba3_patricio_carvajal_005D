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

#RUT, nombre, dirección, comuna, detalle del pedido.
def registrar_p():
    nombre = input('Ingrese su nombre: ')
    direccion = input('ingrese su dirección: ')
    comuna = input('Ingrese su comuna')

    print('Valor 5KG=12500$ Valor 15KG=22500$')
    while True:
        try:
            galon_g = int(input('Ingrese el galon de gas a solicitar, 1)5KG 2)15KG'))
        except:
            print("ERROR DEBE SER UN NUMERO ENTERO!!")
        if galon_g == 1:
            t_venta = galon_g*12500
        elif galon_g == 2:
            t_venta = galon_g*22500

        salir = int(input('Desea agregar mas productos  1)si  2)no: '))
        if salir == 2:
            break
def listar_todos_p():
    pass
def buscar_p_por_rut():
    pass
def imprimir_hoja_ruta():
    pass
def salir_p():
    print('Hasta Pronto!')
    exit()