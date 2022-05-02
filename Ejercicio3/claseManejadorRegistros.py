import csv
from claseRegistro import Registro

class ManejadorRegistros:

    def __init__(self):
        dias = 30
        horas = 24
        self.__listaRegistros = [] ### Ordenado por dias (filas)
        for i in range(dias):
            self.__listaRegistros.append([])
            for j in range(horas):
                self.__listaRegistros[i].append(0)

    def agregaRegistro(self,d,h,regis):
        self.__listaRegistros[d-1].insert(h,regis)

    def cargaRegistros(self):
        archivo = open('Registros.csv')
        reader = csv.reader(archivo,delimiter=',')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                d = int(fila[0])
                h = int(fila[1])
                unRegistro = Registro(int(fila[2]),int(fila[3]),int(fila[4]))
                self.agregaRegistro(d,h,unRegistro)
        archivo.close()

    def test(self):
        print('Funcion test.')
        print('Carga de un registro')
        print('Temperatura (°C): "32 grados". Humedad (%): "45". Presion (hPa): "1013"')
        testregistro = Registro(int(32),int(45),int(1013))
        print('Registro cargado.')
        print('------------------------------------------')
        print('Muestra de registro.')
        print('Temperatura (°C) | Humedad (%) | Presion (hPa)')
        print(testregistro)
        print('-------FIN FUNCION TEST-------')

    def calculaMenorValor(self):
        print('Menores valores registrados.')
        print('----------------------------------------------')
        print('Variable: Temperatura.')
        min = self.__listaRegistros[0][0].getTemperatura()
        diamin = 1
        horamin = 0
        for i in range(len(self.__listaRegistros)):
            for j in range(len(self.__listaRegistros[i])):
                if type(self.__listaRegistros[i][j]) is Registro:
                    if self.__listaRegistros[i][j].getTemperatura() < min:
                        min = self.__listaRegistros[i][j].getTemperatura()
                        diamin = i
                        horamin = j
        print('Menor valor encontrado: {} °C'.format(min))
        print('Día en que se registro: {}'.format(diamin + 1))
        print('Hora: {} hs.'.format(horamin))
        print('----------------------------------------------')
        print('Variable: Humedad.')
        min = self.__listaRegistros[0][0].getHumedad()
        diamin = 1
        horamin = 0
        for i in range(len(self.__listaRegistros)):
            for j in range(len(self.__listaRegistros[i])):
                if type(self.__listaRegistros[i][j]) is Registro:
                    if self.__listaRegistros[i][j].getHumedad() < min:
                        min = self.__listaRegistros[i][j].getHumedad()
                        diamin = i
                        horamin = j
        print('Menor valor encontrado: {} %'.format(min))
        print('Día en que se registro: {}'.format(diamin + 1))
        print('Hora: {} hs.'.format(horamin))
        print('----------------------------------------------')
        print('Variable: Presion.')
        min = self.__listaRegistros[0][0].getPresion()
        diamin = 1
        horamin = 0
        for i in range(len(self.__listaRegistros)):
            for j in range(len(self.__listaRegistros[i])):
                if type(self.__listaRegistros[i][j]) is Registro:
                    if self.__listaRegistros[i][j].getPresion() < min:
                        min = self.__listaRegistros[i][j].getPresion()
                        diamin = i
                        horamin = j
        print('Menor valor encontrado: {} hpA'.format(min))
        print('Día en que se registro: {}'.format(diamin + 1))
        print('Hora: {} hs.'.format(horamin))
        print('----------------------------------------------')

    def calculaMayorValor(self):
        print('Mayores valores registrados.')
        print('----------------------------------------------')
        print('Variable: Temperatura.')
        max = self.__listaRegistros[0][0].getTemperatura()
        diamax = 0
        horamax = 0
        for i in range(len(self.__listaRegistros)):
            for j in range(len(self.__listaRegistros[i])):
                if type(self.__listaRegistros[i][j]) is Registro:
                    if self.__listaRegistros[i][j].getTemperatura() > max:
                        max = self.__listaRegistros[i][j].getTemperatura()
                        diamax = i
                        horamax = j
        print('Mayor valor encontrado: {} °C'.format(max))
        print('Día en que se registro: {}'.format(diamax + 1))
        print('Hora: {} hs.'.format(horamax))
        print('----------------------------------------------')
        print('Variable: Humedad.')
        max = self.__listaRegistros[0][0].getHumedad()
        diamax = 0
        horamax = 0
        for i in range(len(self.__listaRegistros)):
            for j in range(len(self.__listaRegistros[i])):
                if type(self.__listaRegistros[i][j]) is Registro:
                    if self.__listaRegistros[i][j].getHumedad() > max:
                        max = self.__listaRegistros[i][j].getHumedad()
                        diamax = i
                        horamax = j
        print('Mayor valor encontrado: {} %'.format(max))
        print('Día en que se registro: {}'.format(diamax + 1))
        print('Hora: {} hs.'.format(horamax))
        print('----------------------------------------------')
        print('Variable: Presion.')
        max = self.__listaRegistros[0][0].getPresion()
        diamax = 0
        horamax = 0
        for i in range(len(self.__listaRegistros)):
            for j in range(len(self.__listaRegistros[i])):
                if type(self.__listaRegistros[i][j]) is Registro:
                    if self.__listaRegistros[i][j].getPresion() > max:
                        max = self.__listaRegistros[i][j].getPresion()
                        diamax = i
                        horamax = j
        print('Mayor valor encontrado: {} hPa'.format(max))
        print('Día en que se registro: {}'.format(diamax + 1))
        print('Hora: {} hs.'.format(horamax))
        print('----------------------------------------------')

    def temperaturaPromedio(self):
        acum = 0.0 ### Acumulador para el promedio
        hora = 0
        while hora < 24:
            for i in range(len(self.__listaRegistros)):
                if type(self.__listaRegistros[i][hora]) is Registro:
                    acum += self.__listaRegistros[i][hora].getTemperatura()
            print('Promedio mensual de las %d hs.: %.2f ºC' % (hora,acum / len(self.__listaRegistros)))
            acum = 0
            hora += 1
        print('-----------------------------------------------------------')

    def muestraRegistroDia(self):
        numdia = int(input('Ingrese numero de dia:')) - 1
        print('Hora | Temperatura (°C) | Humedad (%) | Presion (hPa)')
        for i in range(24):
            print(' ',i,self.__listaRegistros[numdia][i])
        print('-----------------------------------------------------------')