from random import randint, uniform,random
class Cola (object):
    """Clase que representa una cola, con metodo agregar para agregar elemento, estaVacia para corroborar booleano si esta vacia, y avanzar para eliminar primer elemento y devolver el valor del mismo / El primero de la fila quedaría del lado derecho de la lista  """
    def __init__(self, cola=[]):
        self.cola = []
    def agregar (self,elemento):
        self.cola.insert(0,elemento)
    def avanzar (self):
        return self.cola.pop()
    def estaVacia(self):
        return self.cola == []
    def tamanio(self):
        return len(self.cola)
    def imprimirCola(self):
        print (self.cola)
    def vaciarCola(self):
        while self.tamanio() > 0:
            self.avanzar()
    def darVueltaCola(self):
        aux = []
        while self.tamanio() > 0:
            aux.append(self.avanzar())
        while len(aux) > 0:
            self.agregar(aux.pop())
def pasarANuevaCola(cola):
    nuevaCola = Cola()
    while cola.tamanio() > 0:
        nuevaCola.agregar(cola.avanzar())
    return nuevaCola.cola


def concatenarColas(cola1, cola2):
    nuevaCola = Cola()
    aux = []
    while cola1.tamanio() > 0:
        aux.append(cola1.avanzar())
        nuevaCola.agregar(aux[len(aux)-1])
    while len(aux) > 0:
        cola1.agregar(aux.pop())
    cola1.darVueltaCola()
    while cola2.tamanio() > 0:
        aux.append(cola2.avanzar())
        nuevaCola.agregar(aux[len(aux)-1])
    while len(aux) > 0:
        cola2.agregar(aux.pop())
    cola2.darVueltaCola()
    return nuevaCola.cola
    
def intercambiarColas(cola1,cola2):
    aTransferirDe1 = cola1.tamanio()
    aTransferirDe2 = cola2.tamanio()
    for i in range (aTransferirDe2):
        cola1.agregar(cola2.avanzar())
    for i in range (aTransferirDe1):
        cola2.agregar(cola1.avanzar())
        
"""
def juegoDeLasSillas(participantes):
    sillas = Cola()
    for i in participantes:
        sillas.agregar(i)
    while sillas.tamanio() > 0:
        parado = sillas.avanzar()
        for i in range (randint(10)):
            sillas.agregar(parado)
            parado = sillas.avanzar()
        
"""            
            
        
        

Cola1 = Cola()
print ("La cola esta vacia", Cola1.estaVacia(), "(debería ser true)") 
Cola1.agregar(1)
Cola1.agregar(2)
Cola1.agregar(3)
print(Cola1.avanzar(),"(debería ser 1)")
print (Cola1.cola, "(debería ser [3,2])")
print ("La cola esta vacia", Cola1.estaVacia(),"(debería ser false)")
Cola1.darVueltaCola()
print (Cola1.cola,"debería dar [2,3]")
Cola1.imprimirCola()
Cola1.vaciarCola()
Cola1.imprimirCola()
print("la anterior debería estar vacía")
Cola1.agregar(1)
Cola1.agregar(2)
Cola1.agregar(3)
print(pasarANuevaCola(Cola1))
print ("lo anterior devuelve una cola nueva con el mismo orden que la original")
Cola1.imprimirCola()
print("la cola original quedó vacía")

Cola1.agregar(1)
Cola1.agregar(2)
Cola1.agregar(3)
Cola2 = Cola()
Cola2.agregar(4)
Cola2.agregar(5)
Cola2.agregar(6)
print(concatenarColas(Cola1,Cola2), "las dos colas concatenadas")
print ("como queda la cola1 después de concatenar:")
Cola1.imprimirCola()
print ("como queda la cola2 después de concatenar:")
Cola2.imprimirCola()

intercambiarColas(Cola1,Cola2)
print ("como queda la cola1 después de intercambiar:")
Cola1.imprimirCola()
print ("como queda la cola2 después de intercambiar:")
Cola2.imprimirCola()
