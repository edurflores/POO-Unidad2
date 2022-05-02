from claseManejadorViajeros import ManejadorViajeros

class MenuViajero:
    __switcher = None
    __indiceviajero = ''
    def __init__(self,mv, indviaj):
        self.__switcher = {
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '0':self.salirmenv
        }
        if type(mv) is ManejadorViajeros: ### Recibe el manejador
            self.__manejadorViaj = mv
        else:
            print('Error de parametros.')
        if type(indviaj) is int:
            self.__indiceviajero = indviaj ### Recibe el indice de viajero
        else:
            print('Error de parametro.')
    def opcion(self,op):
        func = self.__switcher.get(op, lambda: print('Error. Opcion no valida.'))
        func()

    def opcion1(self):
        print('Cantidad total de millas: {}'.format(self.__manejadorViaj.MuestraMillas(self.__indiceviajero)))
        print('---------------------------------')

    def opcion2(self):
        mil = int(input('Ingrese cantidad de millas a acumular:'))
        print('Cantidad actual de millas: {}'.format(self.__manejadorViaj.AcumulaMillas(self.__indiceviajero, mil)))
        print('---------------------------------')

    def opcion3(self):
        mil = int(input('Ingrese cantidad de millas a canjear:'))
        print('Cantidad actual de millas: {}'.format(self.__manejadorViaj.CanjeaMillas(self.__indiceviajero, mil)))
        print('---------------------------------')

    def salirmenv(self):
        print('Salio del menu de viajero.')