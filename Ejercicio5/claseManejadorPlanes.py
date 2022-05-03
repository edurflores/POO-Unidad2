import csv
from clasePlanAhorro import PlanAhorro

class ManejadorPlanes:

    def __init__(self):
        self.__listaPlanes = []

    def agregaPlan(self, plan):
        self.__listaPlanes.append(plan)

    def testPlanes(self):
        archivo = open('planes.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                unPlan = PlanAhorro(fila[0],fila[1],fila[2],float(fila[3]))
                self.agregaPlan(unPlan)
        archivo.close()
        print('Se han cargado los planes de ahorro')

    def listarVehiculoMasBaratoValor(self): ### Inciso 2 b.
        print('Listar vehiculos con valor inferior al dado.')
        valor = int(input('Ingrese valor:'))
        for i in range(len(self.__listaPlanes)):
            if self.__listaPlanes[i].getValor() < valor:
                print(self.__listaPlanes[i])
                print('------------------------------------------------')

    def actualizarValorVehiculo(self): ### Inciso 2 a.
        for i in range(len(self.__listaPlanes)):
            print(self.__listaPlanes[i])
            nuevovalor = float(input('Ingrese nuevo valor de vehiculo:'))
            self.__listaPlanes[i].setValor(nuevovalor)
            print('------------------------------------')

    def montoPagarLicitar(self): ### Inciso 2 c.
        print('Monto a pagar para licitar cada vehiculo.')
        for i in range(len(self.__listaPlanes)):
            print('Vehiculo nro. {}'.format(i+1))
            print('-----------------')
            print(self.__listaPlanes[i])
            importecuota = self.__listaPlanes[i].getValor() / PlanAhorro.getCantidadCuotas()
            print('Monto a pagar para licitar el vehiculo: %.2f' % (PlanAhorro.getCantCuotasLicit() * importecuota))
            print('---------------------------------------------------')
