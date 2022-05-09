from claseManejadorCamas import ManejadorCamas
from claseManejadorMedicamentos import ManejadorMedicamentos

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1': self.opcion1,
            '2': self.opcion2,
            '0': self.salir
        }
        self.__mm = ManejadorMedicamentos()
        self.__mm.testMedicamentos()
        self.__mc = ManejadorCamas()
        self.__mc.testCamas()

    def opcion(self,opc):
        func = self.__switcher.get(opc, lambda: print('Error. Opcion no valida.'))
        func()

    def salir(self):
        print('Salio del programa.')

    def opcion1(self):
        print('Ingrese Apellido, Nombre del paciente para dar el alta.')
        print('Ejemplo: "Perez, Luis"')
        nomape = input('Apellido, Nombre:')
        print('--------------------------------------------------------------------------------')
        indice = self.__mc.buscaPaciente(nomape) ### Nota: el idcama del archivo camas coincide con el indice + 1 del arreglo
        if indice != -1:
            print('Informe del paciente dado de alta.')
            print('---------------------------------------------')
            self.__mc.muestraInforme(indice) ### Muestra informe del paciente
            self.__mc.dardeAlta(indice)
            self.__mm.muestraInformeMedicamentos(indice + 1)
        else:
            print('Error, paciente no encontrado.')

    def opcion2(self):
        diag = input('Ingrese diagnostico:')
        self.__mc.muestraPacientesDiagnostico(diag)