class Ventana:
    __titulo = ''
    __xsupizq = 0 ### x superior izquierdo
    __ysupizq = 0 ### y superior izquierdo
    __xinfder = 0 ### x inferior derecho
    __yinfder = 0 ### y inferior derecho

    def __init__(self,tit='',xsi=0,ysi=0,xid=500,yid=500):
        self.__titulo = tit
        if type(xsi) is int:
            self.__xsupizq = xsi
        else:
            print('Error de parametro xsi.')
        if type(ysi) is int:
            self.__ysupizq = ysi
        else:
            print('Error de parametro ysi.')
        if type(xid) is int:
            self.__xinfder = xid
        else:
            print('Error de parametro xid.')
        if type(yid) is int:
            self.__yinfder = yid
        else:
            print('Error de parametro yid.')
        self.normaliza()

    def normaliza(self): ### Aca se aplican las reglas del negocio
        ### Regla de negocio 1: Coordenadas de vertice superior izquierdo no pueden ser menores a 0
        while self.__xsupizq < 0:
            self.__xsupizq += 50
        while self.__ysupizq < 0:
            self.__ysupizq += 50
        ### Regla de negocio 2: Coordenadas de vertice inferior derecho no pueden ser mayores a 500
        while self.__xinfder > 500:
            self.__xinfder -= 500
        while self.__yinfder > 500:
            self.__yinfder -= 500
        ### Regla de negocio 4: El valor de x superior izquierdo debe ser menor al del inferior derecho
        while self.__xsupizq > self.__xinfder:
            self.__xsupizq -= self.__xinfder
        ### Regla de negocio 5: El valor de y superior izquierdo debe ser menor al del inferior derecho
        while self.__ysupizq > self.__yinfder:
            self.__ysupizq -= self.__yinfder

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        return '(' + str(self.__xsupizq) + ',' + str(self.__ysupizq) + ')'

    def ancho(self):
        return '(' + str(self.__xinfder) + ',' + str(self.__yinfder) + ')'

    def moverDerecha(self,unidad=1):
        if type(unidad) is int:
            self.__xsupizq -= unidad
            self.__xinfder += unidad
        else:
            print('Error de parametro unidad.')
        self.normaliza()

    def moverIzquierda(self,unidad=1):
        if type(unidad) is int:
            self.__xsupizq -= unidad
            self.__xinfder += unidad
        else:
            print('Error de parametro unidad.')
        self.normaliza()

    def bajar(self,unidad=1):
        if type(unidad) is int:
            self.__ysupizq -= unidad
            self.__yinfder += unidad
        else:
            print('Error de parametro unidad.')
        self.normaliza()

    def subir(self,unidad=1):
        if type(unidad) is int:
            self.__ysupizq += unidad
            self.__yinfder -= unidad
        else:
            print('Error de paraemtro unidad.')
        self.normaliza()

    def mostrar(self):
        print('X superior izquierdo:{}'.format(self.__xsupizq))
        print('Y superior izquierdo:{}'.format(self.__ysupizq))
        print('X inferior derecho:{}'.format(self.__xinfder))
        print('Y inferior derecho:{}'.format(self.__yinfder))
