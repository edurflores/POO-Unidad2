class ViajeroFrecuente:
    __num_viajero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0

    def __init__(self,num,docu,nomb,ape,millas):
        self.__num_viajero = int(num)
        self.__dni = docu
        self.__nombre = nomb
        self.__apellido = ape
        self.__millas_acum = int(millas)

    def cantidadTotaldeMillas(self):
        return self.__millas_acum

    def acumularMillas(self,sumamillas):
        if type(sumamillas) is int:
            self.__millas_acum += sumamillas
        else:
            print('Error. No se pudo acumular millas.')
        return self.__millas_acum

    def canjearMillas(self,millascanje):
        if type(millascanje) is int:
            if millascanje <= self.__millas_acum:
                self.__millas_acum -= millascanje
            else:
                print('Error. Las millas acumuladas son insuficientes. No puede canjearse.')
        else:
            print('Error. No se puede realizar la operacion, las millas a canjear no estan como int.')
        return self.__millas_acum

    def __str__(self):
        return 'Numero de viajero: ' + str(self.__num_viajero) + ' | DNI: ' + self.__dni + ' | Nombre: ' + self.__nombre + ' | Apellido: ' + self.__apellido + ' | Millas acumuladas: ' + str(self.__millas_acum)

    def getNumeroViajero(self):
        return self.__num_viajero