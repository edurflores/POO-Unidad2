class Conjunto:
    __elementos = None
    def __init__(self,elem):
        if type(elem) is list:
            self.__elementos = elem
        else:
            print('Error de parametros.')

    def getTamanho(self):
        return len(self.__elementos)

    def getElementos(self):
        return self.__elementos

    def muestra(self):
        print(self.__elementos)

    def __add__(self, xconj2): ### Sobrecarga de operador suma para implementar Union de conjuntos.
        nuevoconj = self.__elementos.copy() ### Copia de lista (ver documentacion)
        i = 0
        while i < len(nuevoconj): ### Situacion en que un conjunto tiene varios elementos iguales
            cont = nuevoconj.count(nuevoconj[i])
            while cont > 1: ### El elemento esta repetido (se encuentra mas de una vez)
                nuevoconj.remove(nuevoconj[i]) ### Lo elimina
                cont -= 1
            i += 1
        for j in range(xconj2.getTamanho()): ### Recorre el segundo conjunto comparando cada elemento
            i = 0
            ban = False
            while i < len(nuevoconj) and ban == False:
                if xconj2.getElementos()[j] == nuevoconj[i]:
                    ban = True  ### El elemento ya se encuentra y no hace falta agregarlo.
                else:
                    i += 1
            if ban == False:
                nuevoconj.append(xconj2.getElementos()[j])
        return Conjunto(nuevoconj)

    def __sub__(self, xconj2): ### Sobrecarga de operador resta para implementar diferencia de conjuntos
        nuevoconj = []
        for i in range(len(self.__elementos)):
            j = 0
            ban = False ### True si esta en el segundo conjunto. False si no esta
            while j < xconj2.getTamanho() and not ban:
                if self.__elementos[i] == xconj2.getElementos()[j]:
                    ban = True
                else:
                    j += 1
            if ban == False:
                nuevoconj.append(self.__elementos[i])
        return Conjunto(nuevoconj)



    def __eq__(self, xconj2):
        tconj1 = len(self.__elementos) ### Tamanho de conjuntos
        tconj2 = xconj2.getTamanho()
        self.__elementos.sort() ### Ordena
        xconj2.getElementos().sort() ### Ordena
        i = j = 0
        ban = True ### Bandera con el resultado (son iguales o no son iguales)
        if tconj1 == tconj2: ### Primera condicion, ambos conjuntos deben tener el mismo tamanho.
            while i < tconj1 and ban:
                if self.__elementos[i] == xconj2.getElementos()[j]: ### Elementos iguales
                    i += 1
                    j += 1
                else:
                    ban = False ### Elementos no son iguales
        else:
            ban = False ### No son iguales (no tienen el mismo tamanho)

        return ban ### Resultado