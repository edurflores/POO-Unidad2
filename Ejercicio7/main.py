from claseMenu import Menu

if __name__ == '__main__':
    menu = Menu()

    bandera = False
    while not bandera:
        print('\nMenu principal.')
        print('-------------------')
        print('1- Comparar cantidad de millas con un valor.\n2- Acumular millas.\n3- Canjear millas.')
        print('0- Salir.')
        op = input('Seleccione opcion:')
        menu.opcion(op)
        bandera = op == '0'