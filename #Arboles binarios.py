#Arboles binarios

class Nodo:

    def __init__(self, data):
        self.dato = data
        self.izquierda = None
        self.derecha = None

class Arbol_binario:

    def __init__(self):
        self.head = None

    def insertar(self, data):
        nuevo = Nodo(data)

        if self.head is not None:
            if data < self.head:

                if self.head.izquierda is None:
                    self.head.izquierda = nuevo

                else:
                    self.head.insertar(self.head.izquierda , data)
                
                if self.head.derecha is None
                    self.head.derecha = nuevo

                else: 
                    self.head.insertar(self.head.izquierda, data)

        else:
            self.head = nuevo
            self.head.derecha = None
            self.head.izquierda = None

    def Peso_arbol(self):
        contador = 0
        
        while self.head is not none:
            contador+1
            break
        print(contador)

    def Orden_arbol(self):
        
        pass
    def Altura_arbol(self):
        pass


    def imprimir_arbol(self):
        print(self.data)

nuevo = Nodo(10)
nuevo.imprimir_arbol


