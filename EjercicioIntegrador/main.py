from claseMenu import Menu


if __name__ == '__main__':
    menu = Menu()

    ban = False
    while not ban:
        print('Menu principal.')
        print('-------------------------')
        print('1- Dar de alta y mostrar informe de paciente (inciso 3).\n2- Listar datos de pacientes con un diagnostico (inciso 4).\n0- Salir.')
        op = input('Seleccione opcion:')
        menu.opcion(op)
        ban = op == '0'