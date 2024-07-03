from fun import *

while True:
    opc = menu()

    if opc == 1:
        registrar_p()
    elif opc == 2:
        listar_todos_p()
    elif opc == 3:
        buscar_p_por_rut()
    elif opc == 4:
        imprimir_hoja_ruta()
    elif opc == 5:
        salir_p()