import csv
from claseViajeroFrecuente import ViajeroFrecuente

class ManejadorViajeros:

    def __init__(self):
        self.__listaViajeros = []

    def agregaViajero(self,viajero):
        self.__listaViajeros.append(viajero)

    def cargaViajeros(self):
        archivo = open('archivoViajeros.txt')
        reader = csv.reader(archivo, delimiter=',')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                numv = int(fila[0])
                doc = fila[1]
                nom = fila[2]
                ap = fila[3]
                millas = int(fila[4])
                unViajero = ViajeroFrecuente(numv,doc,nom,ap,millas)
                self.agregaViajero(unViajero)
        archivo.close()
        print('Se han cargado los viajeros frecuentes.')

    def buscaViajero(self,num):
        indice = -1 ### No lo encontro
        for i in range(len(self.__listaViajeros)):
            if self.__listaViajeros[i].getNumeroViajero() == num:
                indice = i
        return indice

    def mostrarViajeros(self):
        print('Listado de viajeros frecuentes:')
        print('-------------------------------------------')
        for i in range(len(self.__listaViajeros)):
            print('Viajero nro: {}'.format(i+1))
            print('Numero de viajero: {}'.format(self.__listaViajeros[i].getNumeroViajero()))
            print('DNI: {}'.format(self.__listaViajeros[i].getDocumento()))
            print('Nombre: {}'.format(self.__listaViajeros[i].getNombre()))
            print('Apellido: {}'.format(self.__listaViajeros[i].getApellido()))
            print('Millas acumuladas: {}'.format(self.__listaViajeros[i].cantidadTotaldeMillas()))
            print('-------------------------------------------')

    def MuestraMillas(self,ind):
        return self.__listaViajeros[ind].cantidadTotaldeMillas()

    def AcumulaMillas(self,ind,mil):
        return self.__listaViajeros[ind].acumularMillas(mil)

    def CanjeaMillas(self,ind,mil):
        return self.__listaViajeros[ind].canjearMillas(mil)