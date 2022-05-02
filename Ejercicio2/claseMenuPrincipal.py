from claseManejadorViajeros import ManejadorViajeros
from claseMenuViajero import MenuViajero


class MenuPrincipal:
    __switcher = None
    def __init__(self):
        self.__switcher = {
            '1': self.opcion1,
            '2': self.opcion2,
            '0': self.salir
        }
        self.__mv = ManejadorViajeros()
        self.__mv.test()
        self.__mv.cargaViajeros()

    def opcion(self,op):
        func = self.__switcher.get(op, lambda: print('Error. Opcion no valida.'))
        func()

    def opcion1(self):
        print('Entre a opcion 1')
        self.__mv.mostrarViajeros()

    def opcion2(self):
        print('Entre a opcion 2.')
        num = int(input('Ingrese numero de viajero:'))
        indice = self.__mv.buscaViajero(num) ### Se buscara su posicion en la lista
        if indice != -1: ### Viajero encontrado
            bandera = False
            self.__menuviaj = MenuViajero(self.__mv, indice) ### Inicializa al menu de viajero
            while not bandera:
                print('Menu de viajero')
                print('---------------------------------')
                print('1- Consultar cantidad de millas.\n2- Acumular millas.\n3- Canjear millas.\n0- Salir.')
                opc = input('Seleccione opcion:')
                self.__menuviaj.opcion(opc)
                bandera = opc == '0'
        else:
            print('Error. Viajero no encontrado')

    def salir(self):
        print('Salio del programa.')