#Pto 2
#crea una lista con algunos valores
miLista = [1024, 3, True, 6.5]
#agrega false a la lista
miLista.append(False)
#imprime la lista
print(miLista)
#inserta 4.5 en la posición 2
miLista.insert(2,4.5)
#imprime la lista
print(miLista)
#imprime el último elemento de la lista, al que elimina
print(miLista.pop())
#imprime la lista
print(miLista)
#imprime el elemento en la posición 1 de la lista, al que elimina
print(miLista.pop(1))
#imprime la lista
print(miLista)
#imprime el elemento en la posición 3 de la lista, al que elimnina
miLista.pop(2)
#imprime la lista
print(miLista)
#ordena la lista ascentendemente
miLista.sort()
#imprime la lista
print(miLista)
#invierte el orden de la lista
miLista.reverse()
#imprime la lista
print(miLista)
#cuenta la cant de veces que 6.5 está en la lista
print(miLista.count(6.5))
#indica la posición de la primera aparición de 4.5 en la lista
print(miLista.index(4.5))
#elimina la primera aparición de 6.5 de la lista
miLista.remove(6.5)
#imprime la lista
print(miLista)
#elimina de la lista el elemento del indice 0
del miLista[0]
#imprime la lista
print(miLista)

"""Otro pto 2: El problema está en la línea 2, el error es de sintáxis, se escibió in in en lugar de i in.
El otro problema es que el índice se sale del rango (en el for, i llega a valer más que el largo de la lista)"""
a=[3,3,3,3,3,3,3,3,3]
for i in range (9):
    print(a[i])

#pto 3
def cuantosPares(lista):
    pares = 0
    for i in range(len(lista)):
        if (lista[i]%2==0):
            pares=pares+1
    return pares
print("hay ",cuantosPares([5,4,6,2,8,2,1])," pares")

#pto 4
def sumaLista(lista):
    resultado=0
    for i in range (len(lista)):
        resultado=resultado+lista[i]
    return resultado
print(sumaLista([3,4,5]))

def multiplicaLista(lista):
    resultado=1
    for i in range (len(lista)):
        resultado=resultado*lista[i]
    return resultado
print(multiplicaLista([3,4,5]))

#pto 5
def maximoEnLista(lista):
    maximo = lista[0]
    for i in range (len(lista)-1):
        if lista[i]>lista[i+1]:
            maximo = lista[i]
        else:
            maximo =lista[i+1]
    return maximo
print(maximoEnLista([3,6,8,9,11]))

#pto 6
"""Toma una lista de palabras y un entero n y borra de la lista las palabras que tienen menos de n caractéres
Pone en una lista aRemover las palabras a eliminar en la medida que va recorriendo la lista original. Cuando termina de 
recorrerla las elimina (Esto porque si directamente eliminaba dentro del recorrido me quedaba index out of range porque 
trataba de recorrer el tamaño original de la lista, que se había ido achicando con cada eliminación)"""
def filtrarPalabrasn(lista, n):
    aRemover = []
    for i in range (len(lista)):
        if len(lista[i]) < n:
            aRemover.append(lista[i])
    for i in aRemover:    
        lista.remove(i)
filtrarPalabrasn(["Juan","Lautaro","Joe","Ryan","Marcos"],5)

#pto 7
"""Sería mejor recibir directamente listas, pero las convertí para respetar el texto de la consigna"""
def productoEscalar(vector1,vector2):
    lista1 = []
    lista2 = []
    devolver = []
    sumaDevolver = 0
    for i in vector1:
        lista1.append(i)
    for i in vector2:
        lista2.append(i)
    for i in range (len(lista1)):
        devolver.append(lista1[i]*lista2[i])
    for i in devolver:
        sumaDevolver = sumaDevolver + i
    return sumaDevolver

print(productoEscalar((1,2,3),(-1,0,2)))

#pto 8
def elimina_duplicados(lista):
    devolver = lista
    for e in devolver:
        for i in range(devolver.count(e)-1):
            devolver.remove(e)
    return devolver
print(elimina_duplicados(["tun","perro","langostino","gato","tun","tun","perro"]))


