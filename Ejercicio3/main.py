from claseMenu import Menu

if __name__ == '__main__':
    menuprinc = Menu()

    bandera = False
    while not bandera:
        print('Menu principal')
        print('------------------')
        print('1- Mostrar para cada variable el dia y hora de menor y mayor valor.\n2- Indicar temperatura promedio mensual por hora.\n3- Listar variables para dia dado.\n0- Salir.')
        opc = input('Seleccione opcion:')
        menuprinc.opcion(opc)
        bandera = opc == '0'