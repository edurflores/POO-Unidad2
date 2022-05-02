class Registro:
    __temperatura = 0
    __humedad = 0 ### Suponer que son todos valores enteros
    __presion = 0

    def __init__(self,temp,hum,pres):
        if type(temp) is int:
            self.__temperatura = temp
        if type(hum) is int:
            self.__humedad = hum
        if type(pres) is int:
            self.__presion = pres

    def __str__(self):
        return '         ' + str(self.__temperatura) + '               ' + str(self.__humedad) + '            ' + str(self.__presion)

    def getTemperatura(self):
        return self.__temperatura

    def getHumedad(self):
        return self.__humedad

    def getPresion(self):
        return self.__presion