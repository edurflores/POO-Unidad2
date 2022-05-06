from claseMenu import Menu

if __name__ == '__main__':
    menu = Menu()
    menu.inicializa()

    bandera = False
    while not bandera:
        print('Menu Principal')
        print('-------------------------')
        print('1- Union de conjuntos.\n2- Diferencia de conjuntos.\n3- Verificar si conjuntos son iguales.\n0- Salir.')
        op = input('Seleccione opcion:')
        menu.opcion(op)
        bandera = op == '0'