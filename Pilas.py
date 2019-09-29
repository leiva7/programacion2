#Pto 1 y 2
class Pila (object):
    """Clase que representa una pila, con metodo push para agregar elemento, top para consultar ultimo elemento, is_empty para corroborar booleano si esta vacia, y pop para eliminar ultimo elemento """
    def __init__(self,pila=[]):
        self.pila = []
    def push(self,elemento):
        self.pila.append(elemento)
    def top(self):
        return self.pila[len(self.pila)-1]
    def is_empty(self):
        #Debería poner solamente return self.pila==[]
        return self.pila==[]
        '''if self.pila == []:
            return True
        else:
            return False'''
    def inspeccionar(self):
        return self.pila[len(self.pila)-1]
    def pop(self):
        return self.pila.pop()
    def tamanio(self):
        return len(self.pila)
    def vaciarPila(self):
        while self.is_empty() == False:
            self.pop()
    def mostrar(self):
    	mostrar = []
    	pilaAuxiliar = Pila()
    	while self.is_empty() == False:
    		pilaAuxiliar.push(self.pop())
    	while pilaAuxiliar.is_empty()==False:
    		mostrar.append(pilaAuxiliar.inspeccionar())
    		self.push(pilaAuxiliar.pop())
    	return mostrar
        
    def darVuelta(self):
    #Esto seguramente no es eficiente pero la otra forma que se me ocurre (comentada abajo) no funciona porque al asignar "invertida" a self, considera que estoy metiendo una pila adentro de otra. En eśta forma con dos pilas auxiliares se va trasladando hasta volver a la primera tipo torre de hannoi.
        pilaAux1 = Pila()
        pilaAux2 = Pila()
        while self.is_empty() == False:
            pilaAux1.push(self.pop())
        while pilaAux1.is_empty() == False:
            pilaAux2.push(pilaAux1.pop())
        while pilaAux2.is_empty() == False:
            self.push(pilaAux2.pop())
   
'''    def darVuelta(self):
#Aparentemente no funciona porque self.pila = invertida asigna una pila anidada adentro de otra
        invertida = Pila()
        while self.is_empty() == False:
            invertida.push(self.pop())
        self.pila = invertida   '''

#Pto 3
def revertirCadena(cadena):
    #Toma una cadena y convierte cada palabra en elementos de una pila; despupes hace pop con cada uno hasta vaciarla, y en la medida que lo hace los agrega a un string para devolverlo
    pilaAux=Pila()
    for i in (cadena.split(" ")):
        pilaAux.push(i)
    string = ""
    while pilaAux.is_empty() == False:
        string += pilaAux.pop() + " "
    return string

#Pto 4
def igualesCerosQueUnos(cadena):
    #Recibe una cadena e identifica si tiene la misma cantidad de ceros que de unos usando dos pilas auxiliares
    pilaAux1 = Pila()
    pilaAux0 = Pila()
    for c in cadena:
        if c == "0":
            pilaAux0.push(c)
        elif c== "1":
            pilaAux1.push(c)
    if pilaAux1.tamanio() == pilaAux0.tamanio():
        return True
    else:
        return False

#Pto 5
def parentesisBalanceados(expresion):
    #Toma una expresion y determina si para cada paréntesis en un sentido existe otro en su opuesto
    pilaDeApertura = Pila()
    for c in expresion:
        if c == "(":
            pilaDeApertura.push(c)
        elif c == ")":
            try:
                pilaDeApertura.pop()
            except IndexError:
                return False
            
    if pilaDeApertura.tamanio()== 0:
        return True
    else:
        return False

#Pto 6
def validezCadenaDeParentesis(expresion):
    #Toma una expresion y determina si parentesis, llaves y corchetes están correctamente balanceados y ordenados con ayuda de pilas
    pilaDeApertura = Pila()
    for c in expresion:
        if c == "(" or c=="[" or c=="{":
            pilaDeApertura.push(c)
        elif (c == ")" and pilaDeApertura.inspeccionar()=="(") or (c == "}" and pilaDeApertura.inspeccionar()=="{") or (c == "]" and pilaDeApertura.inspeccionar()=="[") :
            try:
                pilaDeApertura.pop()
            except IndexError:
                return False   
    if pilaDeApertura.tamanio()== 0:
        return True
    else:
        return False

#Pto 7
def esCapicua(palabra):
    #Toma una palabra y define si es capicua usando pilas; se copian en 2 pilas todos los caracteres de la palabra; se da vuelta una de las pilas; se compara letra por letra hasta que las pilas esten vacias. Si hay alguna letra diferente sale de la función devolviendo falso; si no las va eliminando de ambas pilas. Si llega a las dos listas vacías devuelve verdadero.
    pilaAux = Pila()
    pilaInvert = Pila()
    for c in palabra:
        pilaAux.push(c)
        pilaInvert.push(c)
    pilaInvert.darVuelta()
    while (not pilaInvert.is_empty()) and (not pilaAux.is_empty()):
        if pilaInvert.inspeccionar() != pilaAux.inspeccionar():
            return False
        else:
            pilaInvert.pop()
            pilaAux.pop()
    return True

    

    
p=Pila()
print(p.is_empty())
p.push(4)
p.push("perro")
print(p.inspeccionar())
p.push(True)
print (p.tamanio())
print (p.is_empty())
print (p.pop())
print (p.pop())
print (p.tamanio())
p.vaciarPila()
print (p.tamanio())
p.push(1)
p.push(2)
p.push(3)
p.push(4)
print(p.mostrar())
print(revertirCadena("Mi Diario Python"))
print(igualesCerosQueUnos("ajsndakjsdn0asd1"))
print(parentesisBalanceados("()()()"))
print(parentesisBalanceados("()(()"))
print(parentesisBalanceados("())()"))
print(validezCadenaDeParentesis("{[{8()7}]}"))
print(validezCadenaDeParentesis("{}(){]"))
'''Pila1 = Pila()
print("La pila esta vacia ", Pila1.is_empty())
Pila1.push(7)
Pila1.push(8)
print (Pila1.top())
Pila1.pop()
print (Pila1.top())
print("La pila esta vacia ", Pila1.is_empty())'''
print(esCapicua("ama"))
print(esCapicua("roto"))


#Pto 8
class Pila2(object): #no se por qué no me deja en las definiciones de las funciones usar las funciones de las pilas; tengo que poner .items. ¿por què?
    def __init__(self):
        self.items = []
    def estaVacia(self):
        return self.items == []
    def incluir(self, item):
        self.items.insert(0,item)
    def extraer(self):
        self.items.pop(0)
    def inspeccionar(self):
        return self.items[0]
    def tamano(self):
        return len(self.items)
 

pilaEnCabecera = Pila2()
pilaEnCabecera.incluir(3)
pilaEnCabecera.incluir(2)
pilaEnCabecera.incluir(1)
print(pilaEnCabecera.items)
pilaComun = Pila()
pilaComun.push(3)
pilaComun.push(2)
pilaComun.push(1)
print(pilaComun.mostrar())
pilaEnCabecera.extraer()
print(pilaEnCabecera.items)


class Cola (object):
	"""Clase que representa una cola, con metodo encolar para agregar elemento, is_empty para corroborar booleano si esta vacia, y desencolar para eliminar primer elemento y devolver el valor del mismo  """
	def __init__(self, cola=[]):
		self.cola = []
	def encolar (self,elemento):
		self.cola.append(elemento)
	def desencolar (self):
		devolver = self.cola[0]
		self.cola.pop(0)
		return devolver
	def is_empty(self):
		if self.cola == []:
			return True
		else:
			return False

'''Cola1 = Cola()
print ("La cola esta vacia", Cola1.is_empty())
Cola1.encolar(1)
Cola1.encolar(2)
Cola1.encolar(3)
print(Cola1.desencolar())
print (Cola1.cola)
print ("La cola esta vacia", Cola1.is_empty())'''
	
