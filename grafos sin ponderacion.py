# implementation of an undirected graph using Adjacency Lists
class Vertice:
	def __init__(self, nombre):
		self.nombre = nombre
		self.vecinos = list()
	
	def agregarVecino(self, vecino):
		if vecino not in self.vecinos:
			self.vecinos.append(vecino)
			self.vecinos.sort()

class Grafo:
	vertices = {}
	
	#Metodo para agregar un vertice al grafo; se fija que el vertice existe como objeto, y que todavia no este agregado en el grafo; en ese caso lo agrega al grafo (al diccionario) y devuelve verdadero. Si no devuelve falso
	def agregarVertice(self, vertice):
		if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
			self.vertices[vertice.nombre] = vertice
			return True
		else:
			return False
	
	#Metodo para agregar arista. Se fija si en el diccionario estan los vertices desde y hasta, y en ese caso en la definicion de desde agrega a hasta y viceversa, y devuelve true. En caso de que desde y hasta no esten en el diccionario devuelve false
	def agregarArista(self, d, h):
		if d in self.vertices and h in self.vertices:
			self.vertices[d].agregarVecino(h)
			self.vertices[h].agregarVecino(d)
			return True
		else:
			return False
			
	def imprimirGrafo(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].vecinos))

CI = Grafo()
# print(str(len(g.vertices)))
i = Vertice('2,1')
CI.agregarVertice(i)
##g.agregarVertice(Vertice('B'))
##for i in range(ord('A'), ord('K')):
##	g.agregarVertice(Vertice(chr(i)))
##
##aristas = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
##for arista in aristas:
##	g.agregarArista(arista[:1], arista[1:])

CI.imprimirGrafo()