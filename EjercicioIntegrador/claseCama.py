class Cama:
    __idCama = 0
    __habitacion = ''
    __estado = bool ### True es ocupada, False es libre
    __apellidoNombre = ''
    __diagnostico = ''
    __fechaInternacion= ''
    __fechaAlta = ''

    def __init__(self,idcam,hab,est,apenom,diag,fechaint):
        if type(idcam) is int:
            self.__idCama = idcam
        else:
            print('Error de parametro id cama.')
        self.__habitacion = hab
        if type(est) is bool:
            self.__estado = est
            if est: ### Cama ocupada
                self.__apellidoNombre = apenom
            else:
                self.__apellidoNombre = None ### Porque no esta ocupada
        else:
            print('Error de parametro estado.')
        self.__apellidoNombre = apenom
        self.__diagnostico = diag
        self.__fechaInternacion = fechaint
        self.__fechaAlta = None

    def getNomApePaciente(self):
        return self.__apellidoNombre

    def setNomApePaciente(self,nomape):
        self.__apellidoNombre = nomape

    def getIdcama(self):
        return self.__idCama

    def getHabitacion(self):
        return self.__habitacion

    def getDiagnostico(self):
        return self.__diagnostico

    def getFechaInter(self):
        return self.__fechaInternacion

    def getFechaAlta(self):
        return self.__fechaAlta

    def getEstado(self):
        return self.__estado

    def setEstado(self,nuevoestado):
        if type(nuevoestado) is bool:
            self.__estado = nuevoestado
        else:
            print('Error de parametro estado (debe ser booleano).')

    def setFechaAlta(self,fechalta):
        self.__fechaAlta = fechalta

    def __str__(self): ### Para devolver en el informe por diagnostico
        return self.__apellidoNombre + ' \t' + str(self.__idCama) + '\t    ' + self.__habitacion + '\t\t\t ' + self.__fechaInternacion