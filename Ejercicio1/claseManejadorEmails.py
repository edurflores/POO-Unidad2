import csv
from claseEmail import Email

class ManejadorEmails:
    def __init__(self):
        self.__listaEmails = []

    def AgregarEmail(self, unEmail):
        self.__listaEmails.append(unEmail)

    def IndicaRepetido(self, idcuenta):
        bandera = False
        for i in range(len(self.__listaEmails)):
            if self.__listaEmails[i].getIdCuenta() == idcuenta:
                bandera = True

        if bandera:
            print('El id de cuenta ingresado esta repetido.')
        else:
            print('El id de cuenta ingresado NO esta repetido.')

    def CargaEmails (self):
        archivo = open('Emails.txt')
        reader = csv.reader(archivo,delimiter=',')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                id = fila[0]
                dom = fila[1]
                tdom = fila[2]
                con = fila[3]
                unEmail = Email(id,dom,tdom,con)
                self.AgregarEmail(unEmail)
        archivo.close()
        print('Se han cargado los emails del archivo.')