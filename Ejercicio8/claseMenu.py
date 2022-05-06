from claseConjunto import Conjunto

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '0':self.salir
        }
        self.__conj1 = None ### Conjunto 1
        self.__conj2 = None ### Conjunto 2

    def inicializa(self):
        print('Ingrese elementos (numeros enteros) para el Conjunto 1 separados con coma')
        elems = input('Elementos:')
        elems = elems.split(',')
        for i in range(len(elems)):
            int(elems[i]) ### Los convierte a enteros.
        self.__conj1 = Conjunto(elems) ### Crea el conjunto
        print('Se ha cargado el primer conjunto.')
        print('---------------------------------------')
        print('Ingrese elementos (numeros enteros) para el Conjunto 2 separados con coma')
        elems = input('Elementos:')
        elems = elems.split(',') ### Separa
        for i in range(len(elems)):
            int(elems[i])  ### Los convierte a enteros.
        self.__conj2 = Conjunto(elems) ### Crea el conjunto
        print('Se ha cargado el segundo conjunto.')
        print('---------------------------------------')

    def opcion(self,opc):
        func = self.__switcher.get(opc, lambda:print('Error. Opcion no valida.'))
        func()

    def opcion1(self):
        nuevoconj = self.__conj1 + self.__conj2
        print('Resultado de la union.')
        print('-------------------------')
        nuevoconj.muestra()

    def opcion2(self):
        nuevoconj = self.__conj1 - self.__conj2
        print('Resultado de la diferencia.')
        print('-------------------------')
        nuevoconj.muestra()

    def opcion3(self):
        self.__conj1.muestra()
        self.__conj2.muestra()
        print('-------------------------')
        if self.__conj1 == self.__conj2:
            print('Los conjuntos son iguales.')
        else:
            print('Los conjuntos NO son iguales.')
        print('-------------------------')

    def salir(self):
        print('Salio del programa.')