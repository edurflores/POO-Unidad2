import csv
from claseMedicamento import Medicamento

class ManejadorMedicamentos:

    def __init__(self):
        self.__listaMedicamentos = []

    def agregarMedicamento(self,medi):
        if type(medi) is Medicamento:
            self.__listaMedicamentos.append(medi)
        else:
            print('Error de parametro de clase Medicamento.')

    def testMedicamentos(self):
        archivo = open('medicamentos.csv')
        reader = csv.reader(archivo, delimiter=';')
        ban = True
        for fila in reader:
            if ban:
                ban = not ban
            else:
                unMedicamento = Medicamento(int(fila[0]),int(fila[1]),fila[2],fila[3],fila[4],fila[5],float(fila[6]))
                self.agregarMedicamento(unMedicamento)
        archivo.close()
        print('Se han cargado los datos de medicamentos.')

    def muestraInformeMedicamentos(self,idCama):
        total = 0 ### Acumulador para precio total de los medicamentos
        print('Medicamento/monodroga \t\t Presentacion \t\t Cantidad \t  Precio')
        for i in range(len(self.__listaMedicamentos)):
            if self.__listaMedicamentos[i].getIdCamaMed() == idCama:
                print(self.__listaMedicamentos[i])
                total += self.__listaMedicamentos[i].getPrecioTotal()
        print('Total adeudado: %.2f' % (total))
        print('--------------------------------------------------------------------------------')