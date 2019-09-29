from random import randint, uniform,random
#Guía titulada "Colas,listas,matrices"

#Pto 3 y 4
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

#Pto 5
def pasarANuevaCola(cola):
    nuevaCola = Cola()
    while cola.tamanio() > 0:
        nuevaCola.agregar(cola.avanzar())
    return nuevaCola.cola

#Pto 6
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
    
#Pto 8    
def intercambiarColas(cola1,cola2):
    aTransferirDe1 = cola1.tamanio()
    aTransferirDe2 = cola2.tamanio()
    for i in range (aTransferirDe2):
        cola1.agregar(cola2.avanzar())
    for i in range (aTransferirDe1):
        cola2.agregar(cola1.avanzar())
        
#Pto 9
def juegoDeLasSillas(participantes):
    sillas = Cola()
    for i in participantes:
        sillas.agregar(i)
    while sillas.tamanio() > 0:
        parado = sillas.avanzar()
        for i in range (randint(0,10)):
            sillas.agregar(parado)
            parado = sillas.avanzar()
    return parado
    
juegoDeLasSillas(["Fran","Pau","Facu","Mati"])
          
            
        
        

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


""" Punto 10: por ejemplo podría usarse la cola en un software diseñado para asignar mesas
por orden de llegada en un restaurant, dentro de las que se van desocupando y no se encuentran reservadas"""

class Mesas():
    #True es que la mesa está vacía; están vacías por defecto
    def __init__(self,cantMesas):
        self.mesas = []
        for i in range (cantMesas):
            self.mesas.append(True)
    def cambiarEstado(self,nMesa,estado):
        #NOOSe piensan las mesas como numeradas del 1 al n para no tener mesa 0
        self.mesas[nMesa] = estado
    def ubicar_cliente(self,clientes):
        #se le pasa una cola con clientes
        for m in range (len(self.mesas)):
            if self.mesas[m] == True:
                clientes.avanzar()
                self.cambiarEstado(m,False)
Clientes = Cola()

#Se crea el restaurant La Rueda con 6 mesas
LaRueda = Mesas(6)
print("La Rueda tiene ", len(LaRueda.mesas), " mesas, numeradas del 0 al ", len(LaRueda.mesas)-1)
#Se llenan todas las mesas cuando abre
LaRueda.cambiarEstado(0,False)
LaRueda.cambiarEstado(1,False)
LaRueda.cambiarEstado(2,False)
LaRueda.cambiarEstado(3,False)
LaRueda.cambiarEstado(4,False)
LaRueda.cambiarEstado(5,False)
print(LaRueda.mesas)
#Llegan 4 grupos de clientes
Clientes.agregar("Lopez")
Clientes.agregar("Tulio")
Clientes.agregar("Luque")
Clientes.agregar("Ferreira")
Clientes.imprimirCola()
#Se desocupan la mesa 0 y 4
LaRueda.cambiarEstado(0,True)
LaRueda.cambiarEstado(4,True)
print("Se desocupan la mesa 0 y 4", LaRueda.mesas)
#Se asignan mesas a quienes esperaban
LaRueda.ubicar_cliente(Clientes)
print("Quedan aún sin sentar: ")
Clientes.imprimirCola()
print("La situación de las mesas del restaurante es: ", LaRueda.mesas)
    
