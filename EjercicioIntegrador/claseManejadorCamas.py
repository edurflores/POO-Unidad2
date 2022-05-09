import datetime
import csv
import numpy as np
from claseCama import Cama

### Un arreglo se estructura con una tupla de enteros (dimension o fila,cantidad de componentes en cada dimension o columna)

class ManejadorCamas:
    __dimension = 1 ### Dimension del arreglo (cantidad de filas)
    __indice = 0 ### Indice que tambien indica cantidad de componentes ocupados
    __totalcomponentes = 0 ### Cantidad total (maxima de componentes) en cada dimension (fila)

    def __init__(self):
        self.__arreCamas = np.empty((self.__dimension,self.__totalcomponentes),dtype=Cama)

    def agregaCama(self,unacama):
        if type(unacama) is Cama:
            if self.__indice == self.__totalcomponentes: ### Se llego al limite del arreglo
                self.__totalcomponentes += 1 ### Se incrementa el tamanho del arreglo
                self.__arreCamas.resize((1, self.__totalcomponentes))
            self.__arreCamas[self.__dimension - 1][self.__indice] = unacama
            self.__indice += 1
        else:
            print('Error de parametro de clase Cama.')

    def testCamas(self):
        archivo = open('camas.csv')
        reader = csv.reader(archivo,delimiter=';')
        ban = True
        for fila in reader:
            if ban:
                ban = not ban
            else:
                unaCama = Cama(int(fila[0]),fila[1],bool(fila[2]),fila[3],fila[4],fila[5])
                self.agregaCama(unaCama)
        archivo.close()
        print('Se han cargado los datos de las camas.')

    def buscaPaciente(self,pac):
        ban = -1
        i = 0
        while i < self.__arreCamas.size and ban == -1:
            if pac.lower() in self.__arreCamas[self.__dimension - 1][i].getNomApePaciente().lower(): ### Lo encontro
                ban = i
            else:
                i += 1
        return ban

    def muestraInforme(self,indice):
        print('Paciente: {} \t\t Cama: {} \t Habitacion: {}'.format(self.__arreCamas[self.__dimension - 1][indice].getNomApePaciente(),str(self.__arreCamas[self.__dimension - 1][indice].getIdcama()),self.__arreCamas[self.__dimension - 1][indice].getHabitacion()))
        print('Diagnostico: {} \t\t Fecha de internacion: {}'.format(self.__arreCamas[self.__dimension - 1][indice].getDiagnostico(),self.__arreCamas[self.__dimension - 1][indice].getFechaInter()))

    def dardeAlta(self,indice): ### Da de alta al paciente y establece la fecha
        self.__arreCamas[self.__dimension - 1][indice].setEstado(False) ### La cama ya no estara ocupada
        fechadealta = datetime.date.today() ### Se le da de alta el dia de hoy
        self.__arreCamas[self.__dimension - 1][indice].setFechaAlta(fechadealta)
        print('Fecha de alta: {}'.format(self.__arreCamas[self.__dimension - 1][indice].getFechaAlta().strftime('%d/%m/%Y'))) ### strftime para los objetos datetime especifica formato de salida
        self.__arreCamas[self.__dimension - 1][indice].setNomApePaciente(None) ### Ya no hay paciente


    def muestraPacientesDiagnostico(self,diagnostico):
        print('Paciente\t |\t Cama | Habitacion | Fecha de internacion')
        print('------------------------------------------------------')
        for i in range(self.__arreCamas.size):
            if self.__arreCamas[self.__dimension - 1][i].getEstado(): ### True, la cama esta ocupada
                if diagnostico.lower() in self.__arreCamas[self.__dimension - 1][i].getDiagnostico().lower(): ### El diagnostico coincide
                    print(self.__arreCamas[self.__dimension - 1][i])
                    print('------------------------------------------------------')