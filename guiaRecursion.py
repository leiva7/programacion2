"""
Recursión numérica
Función factorial
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n-1)

factorial (5)
= 5*factorial (4)
= 5*4*factorial(3)
=5*4*3*factorial(2)
=5*4*3*2*factorial(1)
=5*4*3*2*1*1
=120
"""
def factorial(n):
    if n==1:
        return 1
    else:
        return n*(n-1)
    
print (factorial(5))


"""
Recursión sobre listas
Producto de una lista de números:
product :: Num a => [a] -> a
product []     = 1
product (n:ns) = n * product ns

product [5,2,6,8,3]
=5*product[2,6,8,3]
=5*2*product[6,8,3]
=5*2*6*product[8,3]
=5*2*6*8*product[3]
=5*2*6*8*3*product[]
=5*2*6*8*3*1
=1440
"""
def product(lista):
    if lista == []:
        return 1
    else:
        return lista[0]*product(lista[1:])
print(product([5,2,6,8,3]))


"""
Longitud de una lista:
length :: [a] -> Int
length []     = 0
length (_:xs) = 1 + length xs

lenght [5,2,6,8,3]
=1+length [2,6,8,3]
=1+1+length [6,8,3]
=1+1+1+length [8,3]
=1+1+1+1+length [3]
=1+1+1+1+1+length []
=1+1+1+1+1+0
=5
"""
def length(lista):
    if lista == []:
        return 0
    else:
        return (1 + length(lista[1:]))
print(length([5,2,6,8,3]))


"""
Inversa de una lista:
reverse :: [a] -> [a]
reverse []     = []
reverse (x:xs) = (reverse xs) ++ [x]

reverse [5,2,6,8,3]
= (reverse[2,6,8,3])++5
= ((reverse[6,8,3])++2)++5
= (((reverse[8,3])++6)++2)++5
= ((((reverse[3])++8)++6)++2)++5
= (((((reverse[])++3)++8)++6)++2)++5
= (((([]++3)++8)++6)++2)++5
=[3,8,6,2,5]
"""

def reverse (lista,r=[]):
    if lista == []:
        return []
    else:      
        return reverse(lista[1:])+[lista[0]]
print("reverse de [5,2,6,8,3] es:",reverse([5,2,6,8,3]))  

"""
Recursión sobre varios argumentos: La función sumal
Emparejamiento de elementos (la función sumarl):
sumarl :: [a] -> [a] -> [a]
sumarl []     _      = []
sumarl _      []     = []
sumarl (x:xs) (y:ys) = [x+y] ++ sumarl xs ys

sumarl [5,2,6,8] [10,3,4,2]
=[5+10] ++ sumarl [2,6,8] [3,4,2]
=[5+10] ++ [2+3] ++ sumarl [6,8] [4,2]
=[5+10] ++ [2+3] ++ [6+4] ++ sumarl [8] [2]
=[5+10] ++ [2+3] ++ [6+4] ++ [8+2] ++ sumarl [] []
=[5+10] ++ [2+3] ++ [6+4] ++ [8+2] ++ []
=[15,5,10,10]
"""
def sumarl(listaA,listaB,res=[]):
    if len(listaA)==len(listaB):
        if listaA==[] or listaB==[]:    
            return res
        else:
            res.append(listaA[0]+listaB[0])
            return sumarl(listaA[1:],listaB[1:],res)
    else:
        return "las cadenas no tienen el mismo largo"
        
print(sumarl([5,2,6,8],[10,3,4,2]))

"""
4 Recursión múltiple
Fibonacci
fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-2) + fibonacci (n-1)

fibonacci 5
=            fibonacci(3)                     +                         fibonacci(4)
= (fibonacci(1) + fibonacci(2))               +                 (fibonacci(2) + fibonacci(3))
=       1     + (fibonacci(0) + fibonacci(1)) + (fibonacci(0) + fibonacci(1)) + (fibonacci(1) + fibonacci(2))
=5
"""

def fibonacci (n):
    if n==0 or n==1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)
print("Fibonacci de 5 es: ", fibonacci(5)) 


"""
Subir la escalera

formas n::  Int->Int
formas 1 = 1
formas 2 = 2
formas n = formas(n-1) + formas(n-2)

formas 5
=formas(4)+formas(3)
=(formas(3)+formas(2)) + (formas(2)+formas(1))
=((formas(2)+formas(1))+2) + (2 +1)
=2+1+2+2+1
=8
"""
def formas(n):
    if n==1 or n==2:
        return n
    return formas(n-1) + formas(n-2)
    
print("Formas de 5 es: ", formas (5))



"""
5 Recursión mutua
Par e impar por recursión mutua:
par :: Int -> Bool
par 0 = True
par n = impar (n-1)

impar :: Int -> Bool
impar 0 = False
impar n = par (n-1)

par (7)
= impar (6)
= par(5)
= impar(4)
= par(3)
= impar(2)
= par(1)
= impar(0)
= False

"""
def impar(n):
    if n == 0:
        return False
    else:
        return par(n-1)
        
def par (n):
    if n==0:
        return True
    else:
        return impar(n-1)

print("par de 7 da: ",par(7))
