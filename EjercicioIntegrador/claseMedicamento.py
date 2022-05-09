class Medicamento:
    __idCama = 0
    __idMedicamento = 0
    __nombreComercial = ''
    __monodroga = ''
    __presentacion = ''
    __cantidadaplicada = ''
    __preciototal = 0.0

    def __init__(self,idca,idmed,nomcom,mondro,pres,cantapli,ptotal):
        if type(idca) is int:
            self.__idCama = idca
        else:
            print('Error de parametro idcama.')
        if type(idmed) is int:
            self.__idMedicamento = idmed
        else:
            print('Error de parametro idmedicamento.')
        self.__nombreComercial = nomcom
        self.__monodroga = mondro
        self.__presentacion = pres
        self.__cantidadaplicada = cantapli
        if type(ptotal) is float:
            self.__preciototal = ptotal
        else:
            print('Error de parametro precio total.')

    def getIdCamaMed(self):
        return self.__idCama

    def getPrecioTotal(self):
        return self.__preciototal

    def __str__(self):
        return self.__nombreComercial + ' / ' + self.__monodroga + ' \t\t' + self.__presentacion + ' \t\t\t' + self.__cantidadaplicada + ' \t\t  ' + str(self.__preciototal)