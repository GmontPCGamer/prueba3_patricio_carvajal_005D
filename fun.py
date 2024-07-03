import csv, msvcrt, os
datos_clientes = []
precio_g1 = 12500
precio_g2 = 22500
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
    limpiar_p()
    rut = int(input('Ingrese su rut sin puntos ni guion'))
    nombre = input('Ingrese su nombre: ')
    direccion = input('ingrese su dirección: ')
    comuna = input('Ingrese su comuna')
    print('Valor 5KG=12500$ Valor 15KG=22500$')

    t_venta15 = 0
    t_venta5 = 0
    while True:
        limpiar_p()
        try:
            galon_g = int(input('Ingrese el galon de gas a solicitar, 1)5KG 2)15KG'))
        except:
            print("ERROR DEBE SER UN NUMERO ENTERO!!")
        if galon_g == 1:
            cantidad = int(input('ingrese la cantidad a comprar'))
            t_venta5 = cantidad*precio_g1
        elif galon_g == 2:
            cantidad = int(input('ingrese la cantidad a comprar'))
            t_venta15 = cantidad*precio_g2
        salir = int(input('Desea agregar mas productos  1)si  2)no: '))
        total_c = t_venta15+t_venta5
        datos_cliente = rut,nombre,direccion,comuna,galon_g,t_venta5,t_venta15, total_c
        if salir == 2:
            datos_clientes.append(datos_cliente)
            print('DETALLE')
            print("="*25)
            print("nombre  Dirección  Comuna  Gas.5KG Gas.15KG total")
            for x in range(len(datos_clientes)):
                print(datos_clientes[x])
            print("="*25)
            esperar_t()
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


################
    
def limpiar_p():
    os.system('cls')
def esperar_t():
    print('presione tecla para continuar...')
    msvcrt.getch()