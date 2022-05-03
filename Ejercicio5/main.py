from claseMenuPrincipal import MenuPrincipal

if __name__ == '__main__':
    menu = MenuPrincipal()

    bandera = False
    while not bandera:
        print('\nMenu Principal')
        print('\n1- Actualizar el valor de vehiculo de cada plan.\n2- Mostrar vehiculos con valor inferior al dado.')
        print('3- Mostrar monto a pagar para licitar cada vehiculo.\n4- Modificar cantidad de cuotas pagas para licitar.')
        print('0- Salir')
        opc = input('Seleccione opcion:')
        menu.opcion(opc)
        bandera = opc == '0'
