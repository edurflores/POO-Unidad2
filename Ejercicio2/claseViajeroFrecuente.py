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
            return self.__millas_acum
        else:
            print('Error. No se pudo acumular millas.')
            return self.__millas_acum ### Igual retorna el valor actual

    def canjearMillas(self,millascanje):
        if type(millascanje) is int:
            if millascanje <= self.__millas_acum:
                self.__millas_acum -= millascanje
                return self.__millas_acum
            else:
                print('Error. Las millas acumuladas son insuficientes. No puede canjearse.')
                return self.__millas_acum
        else:
            print('Error. No se puede realizar la operacion, las millas a canjear no estan como int.')

    def getNumeroViajero(self):
        return self.__num_viajero
    def getDocumento(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido