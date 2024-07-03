import csv, msvcrt, os
datos_clientes = []
ruta = ["puentealto", "colina", "laflorida"]
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
    while True:
        try:
            rut = int(input('Ingrese su rut sin puntos ni guion'))
            if rut > 6:
                break
        except:
            print("!ERROR DEBE SER UN NUMERO ENTERO")
    while True:
        nombre = input('Ingrese su nombre: ')
        if len(nombre) > 2:
            break
        else:
            print("Su nombre debe tener mas de 2 caracteres")
            esperar_t
    while True:
        direccion = input('ingrese su dirección: ')
        if len(direccion) > 5:
            break
        else:
            print("Su dirección debe tener mas 5 caracteres")
            esperar_t
    while True:
        try:
            comuna = int(input('Ingrese su comuna, 1)puente alto, 2)colina, 3)La Florida'))
            
            if comuna ==1:
                comuna = "puentealto"
                break
            elif comuna ==2:
                comuna = "colina"
                break
            elif comuna ==3:
                comuna="laflorida"
                break
            else:
                print("ERROR NO ESCOGIO NINGUNA DE LAS COMUNAS")
        except:
            print("ERROR DEBE SER UNA DE LAS 3 OPCIONES")
            esperar_t
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
            while True:
                try:
                    cantidad = int(input('ingrese la cantidad a comprar'))
                    if cantidad > -1:
                        break
                    else:
                        print("Debe ser positivo o 0")
                except:
                    print("ERROR DEBE SER UN NUMERO ENTERO")
            cantidad = int(input('ingrese la cantidad a comprar'))
            t_venta5 = cantidad*precio_g1
        elif galon_g == 2:
            while True:
                try:
                    cantidad = int(input('ingrese la cantidad a comprar'))
                    if cantidad > -1:
                        break
                    else:
                        print("Debe ser positivo o 0")
                except:
                    print("ERROR DEBE SER UN NUMERO ENTERO")
            t_venta15 = cantidad*precio_g2
        salir = int(input('Desea agregar mas productos  1)si  2)no: '))
        total_c = t_venta15+t_venta5
        datos_cliente = rut,nombre,direccion,comuna,galon_g,t_venta5,t_venta15, total_c
        if salir == 2:
            datos_clientes.append(datos_cliente)
            print('DETALLE')
            print("="*25)
            print("nombre  Dirección  Comuna  Gas.5KG Gas.15KG total")
            puesto = 0
            for x in range(len(datos_clientes)):
                puesto += puesto
                print(datos_cliente)
            print("="*25)
            esperar_t()
            break
def listar_todos_p():
    print("="*25)
    print("nombre  Dirección  Comuna  Gas.5KG Gas.15KG total")
    for x in range(len(datos_clientes)):
        print(datos_clientes[x])
    print("="*25)
    esperar_t()
def buscar_p_por_rut():
    buscar_rut = int(input('ingrese rut a buscar'))
    x = 0
    for buscar_rut in range(len(datos_clientes)):
        print(datos_clientes[x])
    with open('archivo_cliente', mode="w", newline="") as archivo:
        writer=csv.writer(archivo)
        writer.writerows(datos_clientes)

def imprimir_hoja_ruta():
    x = 0
    comuna = input("que comuna busca, puentealto, colina, laflorida")
    for comuna in range(len(datos_clientes)):
        print(datos_clientes[x])
def salir_p():
    print('Hasta Pronto!')
    exit()


################
    
def limpiar_p():
    os.system('cls')
def esperar_t():
    print('presione tecla para continuar...')
    msvcrt.getch()