from claseManejadorRegistros import ManejadorRegistros

class Menu:
    __switcher = None
    def __init__(self):
        self.__switcher = {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '0': self.salir
        }
        self.__mr = ManejadorRegistros()
        self.__mr.test()
        self.__mr.cargaRegistros()

    def opcion(self,opc):
        func = self.__switcher.get(opc, lambda: print('Error. Opcion no valida.'))
        func()

    def opcion1(self):
        self.__mr.calculaMenorValor()
        self.__mr.calculaMayorValor()

    def opcion2(self):
        self.__mr.temperaturaPromedio()

    def opcion3(self):
        self.__mr.muestraRegistroDia()

    def salir(self):
        print('Salio del programa.')