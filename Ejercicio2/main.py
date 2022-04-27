from claseManejadorViajeros import ManejadorViajeros

if __name__ == '__main__':
    mv = ManejadorViajeros()
    mv.test()
    mv.cargaViajeros()
    print('Menu principal')
    print('1- Mostrar todos los viajeros.\n2- Ingresar a menu de viajero.\n0- Salir.')
    op = int(input('Seleccione opcion: '))
    while op != 0:
        if op == 1:
            mv.mostrarViajeros()
        elif op == 2:
            num = int(input('Ingrese numero de viajero:'))
            indice = mv.buscaViajero(num)
            if indice != -1: ### Suponiendo que lo encontro
                print('---------------------------------')
                print('Menu de viajero')
                print('---------------------------------')
                print('1- Consultar cantidad de millas.\n2- Acumular millas.\n3- Canjear millas.\n0- Salir.')
                opcion = int(input('Seleccione opcion:'))
                while opcion != 0:
                    if opcion == 1:
                        print('Cantidad total de millas: {}'.format(mv.MuestraMillas(indice)))
                        print('---------------------------------')
                    elif opcion == 2:
                        mil = int(input('Ingrese cantidad de millas a acumular:'))
                        print('Cantidad actual de millas: {}'.format(mv.AcumulaMillas(indice,mil)))
                        print('---------------------------------')
                    elif opcion == 3:
                        mil = int(input('Ingrese cantidad de millas a canjear:'))
                        print('Cantidad actual de millas: {}'.format(mv.CanjeaMillas(indice,mil)))
                        print('---------------------------------')
                    else:
                        print('Error. Opcion incorrecta.')
                    print('1- Consultar cantidad de millas.\n2- Acumular millas.\n3- Canjear millas.\n0- Salir.')
                    opcion = int(input('Seleccione opcion: '))
            else:
                print('Error. Viajero no encontrado.')
        else:
            print('Error. Opcion incorrecta.')
        print('1- Mostrar todos los viajeros.\n2- Ingresar a menu de viajero.\n0- Salir.')
        op = int(input('Seleccione opcion: '))