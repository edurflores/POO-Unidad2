class PlanAhorro:
    __codigoplan = ''
    __modelo = ''
    __versionvehiculo = ''
    __valorvehiculo = 0.0
    cantidadcuotas = 60 ### Variable de clase (dato miembro estatico)
    cantidadcuotaslicitacion = 15 ### Variable de clase (dato miembro estatico)

    def __init__(self,codplan,mod,vers,valor):
        self.__codigoplan = codplan
        self.__modelo = mod
        self.__versionvehiculo = vers
        if type(valor) is float:
            self.__valorvehiculo = valor

    def getValor(self):
        return self.__valorvehiculo
    def __str__(self):
        return 'Codigo: ' + self.__codigoplan + ' | Modelo: ' + self.__modelo + ' | Version: ' + self.__versionvehiculo + ' | Valor: ' + str(self.__valorvehiculo)
    def setValor(self,nuevoval):
        if type(nuevoval) is float:
            self.__valorvehiculo = nuevoval
            print('Valor actualizado.')
        else:
            print('Error. El valor no es del tipo de dato correspondiente.')

    @classmethod
    def getCantidadCuotas(cls):
        return cls.cantidadcuotas
    @classmethod
    def getCantCuotasLicit(cls):
        return cls.cantidadcuotaslicitacion