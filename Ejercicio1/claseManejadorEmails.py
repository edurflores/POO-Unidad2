import csv
from claseEmail import Email

class ManejadorEmails:
    def __init__(self):
        self.__listaEmails = []

    def AgregarEmail(self, unEmail):
        self.__listaEmails.append(unEmail)

    def IndicaRepetido(self, idcuenta):
        i = 0
        bandera = False
        while i < len(self.__listaEmails) and bandera == False:
            if self.__listaEmails[i].getIdCuenta() == idcuenta: ### Lo encontro
                bandera = True
            else:
                i += 1

        if bandera:
            print('El id de cuenta ingresado esta repetido.')
        else:
            print('El id de cuenta ingresado NO esta repetido.')

    def CargaEmails (self):
        archivo = open('archivoEmails.csv')
        reader = csv.reader(archivo,delimiter=',')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                unEmail = Email(fila[0],fila[1],fila[2],fila[3])
                self.AgregarEmail(unEmail)
        archivo.close()
        print('Se han cargado los emails del archivo.')