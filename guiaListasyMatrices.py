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

#Ejercicios matrices

#Pto 1
def crearMatriz(filas,columnas):
    nombre = []
    for i in range(filas):
        nombre.append([])
        for j in range(columnas):
            nombre[i].append(0)
    return nombre
    
a = crearMatriz(2,3)
print(a)

#Pto 2
def devolverFilas(matriz):
    filas = 0
    for i in range (len(matriz)):
        filas += 1
    return filas
    
def devolverColumnas(matriz):
    columnas = 0
    for c in range (len(matriz[0])):
        columnas +=1
    return columnas
        

print(devolverFilas(a)) 
print(devolverColumnas(a))

#Pto 3
def enumF(matriz):
    contador = 1
    for i in range (devolverFilas(matriz)):
        for j in range (devolverColumnas(matriz)):
            matriz[i][j]=contador
            contador +=1
    return matriz  
    
print(enumF(a))

def enumC(matriz):
    contador = 1
    for c in range (devolverColumnas(matriz)):
        for f in range (devolverFilas(matriz)):
            matriz[f][c]=contador
            contador +=1
    return matriz  
    
print(enumC(a))

#Pto 4
def cantPares(matriz):
    contador = 0
    for f in range (devolverFilas(matriz)):
        for c in range (devolverColumnas(matriz)):
            if matriz[f][c]%2==0:
                contador += 1
    return contador
    
print(cantPares(a))

#Pto 5
def sumarMatrices(mA,mB):
    if (devolverFilas(mA)==devolverFilas(mB)) & (devolverColumnas(mA)==devolverColumnas(mB)):
        nueva = crearMatriz(devolverFilas(mA),devolverColumnas(mA))
        for f in range (devolverFilas(mA)):
            for c in range (devolverColumnas(mB)):
                nueva[f][c]=mA[f][c]+mB[f][c]
        return nueva
    else:
        return False

b=crearMatriz(4,4)
print(a)
print(b)
print(sumarMatrices(a,b), "da falso porque las matrices son de distinto tamaño")
c=crearMatriz(2,3)
enumF(c)
print(a)
print(c)
print(sumarMatrices(a,c))

#Pto 6
#Dado que la matriz es cuadrada la cant de filas y columnas son las mismas; como estoy buscando la diagonal (o sea los i 1,1 2,2 3,3 etc) recorro con un solo índice
def diagonal (matrizCuadrada):
    diagonal = []
    for f in range (devolverFilas(matrizCuadrada)):
        diagonal.append(matrizCuadrada[f][f])
    return diagonal
enumF(b)
print(b)
print(diagonal(b))

def sumaDiagonal(matrizCuadrada):
    suma = 0
    for f in range (devolverFilas(matrizCuadrada)):
        suma += (matrizCuadrada[f][f])
    return suma
print("suma diagonal: ")
print(sumaDiagonal(b))

#Pto 7
d = enumF(crearMatriz(5,6))
print("Matriz en la que se buscarán números primos: ")
print (d)

#Devuelve el mismo numero si es primo, y false si no lo es
def es_primo(num):
    for i in range (2,num):
        if num%i ==0:
            return False
    return num
    
#Para cada posición de la matriz, comparo si lo retornado por es_primo es el mismo número. Si es, agrego la posición como tupla a una lista. 
def posiciones_primos(matriz):
    pos = []
    for f in range (devolverFilas(matriz)):
        for c in range (devolverColumnas(matriz)):
            if es_primo(matriz[f][c])==(matriz[f][c]):
                pos.append((f,c))
    return pos
print("Tuplas con las posiciones de los números prímos de la matriz anterior: ")
print(posiciones_primos(d))