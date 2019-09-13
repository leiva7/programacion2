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
