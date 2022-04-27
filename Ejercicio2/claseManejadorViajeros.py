import csv
from claseViajeroFrecuente import ViajeroFrecuente

class ManejadorViajeros:

    def __init__(self):
        self.__listaViajeros = []

    def test(self):
        print('Funcion test.')
        print('Carga de un viajero frecuente.')
        print('Numero de viajero: "18776" , DNI: "177013", Nombre: "Eduardo", Apellido: "Flores", Millas acumuladas: "789"')
        testviajero = ViajeroFrecuente('18876','177013','Eduardo','Flores','789')
        print('Viajero cargado.')
        print(testviajero)
        print('-------FIN FUNCION TEST-------')

    def agregaViajero(self,viajero):
        self.__listaViajeros.append(viajero)

    def cargaViajeros(self):
        archivo = open('archivoViajeros.csv')
        reader = csv.reader(archivo, delimiter=',')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                unViajero = ViajeroFrecuente(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]))
                self.agregaViajero(unViajero)
        archivo.close()
        print('Se han cargado los viajeros frecuentes.')

    def buscaViajero(self,num):
        ban = -1 ### Bandera que hace de indice en caso de que lo encuentre, o -1 si no lo encontro
        i = 0 ### Indice
        while i < len(self.__listaViajeros) and ban == -1:
            if self.__listaViajeros[i].getNumeroViajero() == num: ### Lo encontro
                ban = i
            else:
                i += 1
        return ban

    def mostrarViajeros(self):
        print('Listado de viajeros frecuentes:')
        print('-------------------------------------------')
        for i in range(len(self.__listaViajeros)):
            print(self.__listaViajeros[i])
            print('-------------------------------------------------------------------')

    def MuestraMillas(self,ind):
        return self.__listaViajeros[ind].cantidadTotaldeMillas()

    def AcumulaMillas(self,ind,mil):
        return self.__listaViajeros[ind].acumularMillas(mil)

    def CanjeaMillas(self,ind,mil):
        return self.__listaViajeros[ind].canjearMillas(mil)