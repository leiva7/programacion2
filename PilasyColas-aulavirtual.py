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
        

Cola1 = Cola()
print ("La cola esta vacia", Cola1.estaVacia(), "(debería ser true)") 
Cola1.agregar(1)
Cola1.agregar(2)
Cola1.agregar(3)
print(Cola1.avanzar(),"(debería ser 1)")
print (Cola1.cola, "(debería ser [3,2])")
print ("La cola esta vacia", Cola1.estaVacia(),"(debería ser false)")
	
