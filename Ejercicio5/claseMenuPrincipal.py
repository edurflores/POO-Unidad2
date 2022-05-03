from claseManejadorPlanes import ManejadorPlanes
from clasePlanAhorro import PlanAhorro ### Por inciso 3 d

class MenuPrincipal:
    __switcher = None
    def __init__(self):
        self.__switcher = {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '4': self.opcion4,
            '0': self.salir,
        }
        self.__ManejadorP = ManejadorPlanes()
        self.__ManejadorP.testPlanes() ### Carga para test desde el archivo csv
    def opcion(self,op):
        func = self.__switcher.get(op, lambda: print('Error. Opcion no valida'))
        func()

    def salir(self):
        print('Salio del programa.')

    def opcion1(self):
        self.__ManejadorP.actualizarValorVehiculo()

    def opcion2(self):
        self.__ManejadorP.listarVehiculoMasBaratoValor()

    def opcion3(self):
        self.__ManejadorP.montoPagarLicitar()

    def opcion4(self):
        cant = int(input('Ingrese nueva cantidad de cuotas para licitar:'))
        PlanAhorro.cantidadcuotaslicitacion = cant
        print('Se ha modificado la cantidad de cuotas para licitar. Nueva cantidad: {}'.format(PlanAhorro.getCantCuotasLicit()))