class ListaEnlazada:
    class Nodo:
        def __init__(self, dato):
            self.dato = dato
            self.siguiente = None

    def __init__(self):
        self.primero = None
        self.tamanio = 0
    
    def agregar(self, valor):
        nodo = self.Nodo(valor)
        if self.tamanio == 0:
            self.primero = nodo
        else:
            actual = self.primero
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nodo
        
        self.tamanio += 1

    def agregarInicio(self, dato):
        nodo = self.Nodo(dato)
        if len(self) == 0:
            self.primero = nodo
        else:
            aux = nodo
            aux.siguiente = self.primero
            self.primero = aux

    def eliminarInicio(self):
        if len(self) == 0:
            pass
        elif self.primero.siguiente == None:
            self.primero = None
        else:
            self.primero = self.primero.siguiente
    
    def eliminar(self, valor):
        if self.tamanio == 0:
            return False
        elif valor == self.primero.dato:
            self.primero = self.primero.siguiente
            
        else:
            actual = self.primero
            try:
                while actual.siguiente.dato != valor:
                    actual = actual.siguiente
                
                nodoBorrar = actual.siguiente
                actual.siguiente = nodoBorrar.siguiente
                
            except AttributeError:
                return False
        
        self.tamanio -= 1          
    
    def __len__(self):
        return self.tamanio
    
    def __str__(self):
        cadena = ''
        actual = self.primero
        while actual != None:
            cadena += str(actual.dato)
            cadena += ' ⟶  '
            actual = actual.siguiente
        cadena += 'None'
        
        return cadena
