class Email:
    __idCuenta = ''
    __dominio = ''
    __tipodominio = ''
    __contrasenha = ''

    def __init__(self, idc, dom, tipodom, contra):
        self.__idCuenta = idc
        self.__dominio = dom
        self.__tipodominio = tipodom
        self.__contrasenha = contra

    def getDominio(self):
        return self.__dominio

    def getIdCuenta(self):
        return self.__idCuenta

    def modificaContrasenha(self):
        print('Modificar contrasenha.')
        con = input('Ingrese contrasenha actual:')
        if self.__contrasenha == con:
            nuevacon = input('Ingrese nueva contrasenha:')
            self.__contrasenha = nuevacon
            print('Contrasenha modificada con exito.')
        else:
            print('ERROR. Contrasenha incorrecta.')

    def crearCuenta(self, em):
            email = em.split('@')
            self.__idCuenta = email[0]
            email = email[1].split('.')
            self.__dominio = email[0]
            self.__tipodominio = email[1]
    def retornaEmail(self):
        return self.__idCuenta + '@' + self.__dominio + '.' + self.__tipodominio
