def holaMundo():
	#Imprime Hola Mundo. No toma ni devuelve nada.
	print ("HolaMundo")
	
import random
def sumar(x,y):
	#Devuelve la suma de 2 parametros. Int->Int = Int
	return x+y
	
def mayor(x,y):
	#Devuelve el mayor de dos numeros pasados por parametros. Int->Int = Int
	if x<y:
		return y
	elif x>y:
		return x 
	else:
		return "son iguales" #este no es un int, y si son igualdes devolve cualquiera :)
		
def entre0y10 (x):
	#Devuelve un string indicando si está entre 0 y 10. Int = String
	if x>=0 and x<=10:
		return "El valor indicado esta entre 0 y 10"
	else:
		return "No esta entre 0 y 10"
# Estaria bueno que devuelvas un bool y despues uses eso para imprimir, pero esta bien
		
def entre0y10y20y30 (x):
	#Devuelve un string indicando si está entre 0 y 10. Int = String
	if x>=0 and x<=10:
		return "El valor indicado esta entre 0 y 10"
	elif x>=11 and x<=20:
		return "El valor esta entre 11 y 20"
	elif x>=21 and x<=30:
		return "El valor esta entre 21 y 30"
	else:
		return "Es menor a 0 o mayor a 30"
#idem anterior
		
def unoal100conwhile():
	#Imprime los numeros del 1 al 100 con un while. No toma ni retorna nada.
	i=0
	while i<101:
		print(i)
		i += 1

def unoal100confor():
	#Imprime los numeros del 1 al 100 con un for. No toma ni retorna nada. 
	for i in range (0,101):
			print(i)
			
def caracteresHolaMundo():
	#Impreime cada caracter de hola mundo. No toma ni retorna nada.
	for c in "Hola mundo":
			print (c)
			
def esPar(x):
        #Recibe un numero y determina si es par o no. Int->Bool
        if x%2==0:
                return True
        else:
                return False
def paresDe1a100():
        #Muestra los numeros pares del 1 al 100. No toma ni retorna nada.
        for i in range (0,101):
                if esPar(i):
                        print (i)

def numeroEntre5y10():
        #Genera un numero entre 5 y 10. No toma parametros; retorna Int
        return random.randrange(5,10,1)

def rango10a0():
        #Imprime los numeros del 10 al 0. No toma ni retorna.
        i=10
        while i>=0:
                print (i)
                i -=1

def mulaHondo(palabra1,palabra2):
        # dados dos palabras, muestra ambas palabras separadas por un espacio e intercambiando los dos primeros caracteres. Por ejemplo, hola mundo pasaría a mula hondo. No toma ni retorna.
        print (palabra2[0:2]+palabra1[2:]+" "+palabra1[0:2]+palabra2[2:])

#Testeala , hay problemas con los limites
# mulaHondo("Casa","Perro")
# Pesa Carro

def adivinador(guess):
        #Genera un numero del 1 al 100; compara con lo que adivine el usuario por parametro y devuelve si gano o perdio. Int->no retorna, imprime.
        definido = random.randrange(1,100,1)
        if definido == guess:
                print ("Ganaste")
        else:
                print ("Perdiste, el numero era ", definido)

def max_de_tres(a,b,c):
	#Devuelve el maximo de los 3 parametros. Int->Int->Int = Int
	return max (a, b,c)
# no tiene chiste! jajajja, hacela vos a la funcion :)

def largoLista(lista):
	#Devuelve la cantidad de elementos de una lista o cadena pasada por parametro. [] or string = Int
	contador = 0
	for e in lista:
			contador +=1
	return contador

def esVocal(letra):
	#Toma una vocal y evalua si es o no vocal. char = Bool
	if letra == "a" or letra=="o" or letra=="e" or letra=="i" or letra=="u":
		return True
	else:
		return False
        
def sum(lista):
        #Devuelve la suma de los elementos de la lista. [Int]=Int
	acumulador = 0
	for n in lista:
		acumulador += n
	return acumulador

def multip(lista):
        #Devuelve la multiplicación de los elementos de la lista. [Int]=Int
        acumulador = 1
        for n in lista:
                acumulador = acumulador*n
        return acumulador
def inversa(cadena):
	#Devuelve la cadena invertida. Str = Str
	i=-1
	inversion = ""
	while i>=(-(len(cadena))): #que ganas de complicarte contando patras jajaj :)
		inversion = inversion + cadena[i]
		i -=1
	return inversion
	

def es_palindromo(palabra):
        #Identifica si una palabra es o no palindromo. Str=Bool
        if palabra == inversa(palabra):
                return True
        else:
                return False
#Buenisimooo, usaste la funcion que definiste antes!

def superposicion(lista1, lista2):
        #toma dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. []->[]=Bool
        for i in lista1:
                for j in lista2:
                        if i == j:
                                return True
        return False

def generar_n_caracteres(n,char):
        #Toma un numero y un caracter y devuelve el caracter multiplicado por n. Int->Char=Str
        return n*char

def procedimiento(listaEnt):
         #toma una lista de numeros enteros e imprime un histograma en la pantalla. [Int]=Nada(print)
         for n in listaEnt:
                 print (n*"*")

def decimalaBinario(decimal):
        #Toma un entero positivo y lo convierte en número decimal Int->Int
        #Explicacion como se hace conversion:  http://recursostic.educacion.es/secundaria/edad/4esotecnologia/quincena5/4q2_contenidos_2c.htm
        #Insert uso en lugar de append para agregar por izquierda a la lista
        contadorDeMod = 0
        binario = []
        while decimal > 0:
                contadorDeMod = decimal % 2
                binario.insert(0,(contadorDeMod))
                decimal = int((decimal-contadorDeMod)/2)
        return binario

def binarioaDecimal(binario):
        #Toma un numero binario (representado en int) y devuelve un decimal Int->Int
        #La conversion se hace multiplicando de derecha a izquierda a c/digito del numero binario por 2 a la potencia de 0 en el primero, 1 en el segundo, 2 en el tercero y asi sucecivamente
        decimal = 0
        exp = len((str(binario)))-1
        for n in str(binario):
                decimal = decimal + int(n) *( 2**exp )
                exp -=1
        return decimal
        

holaMundo()
print(sumar(2,5))
print(mayor(2,5))
print (entre0y10(2))
print (entre0y10(11))
print(entre0y10y20y30(9))
print(entre0y10y20y30(11))
print(entre0y10y20y30(25))
print(entre0y10y20y30(120))
#unoal100conwhile()
#unoal100confor()
#caracteresHolaMundo()
print(esPar(2))
print(esPar(5))
#paresDe1a100()
print(numeroEntre5y10())
#rango10a0()
mulaHondo("hola","mundo")
#adivinador(input("adivina un numero del 1 al 100"))
print(max_de_tres(5,12,3))
print(largoLista([5,6,7]))
print(esVocal("a"))
print(esVocal("z"))
print(sum([1,2,3,4]))
print(multip([1,2,3,4]))
print(inversa("Hola"))
print(es_palindromo("ama"))
print(es_palindromo("Laura"))
print(superposicion([1,2,3],[4,5,6]))
print(superposicion([1,2,3],[4,5,1]))
print (generar_n_caracteres(3,"J"))
procedimiento([2,3,4])
print(decimalaBinario(28))
print(binarioaDecimal(11100))

print ("Punto 26")
print ("a)suma todos los enteros del 0 a n. def sumatoriaN.")
print ("b)suma todos los enteros del 0 a n. def sumatoriaNrecursiva.")
print ("c)multiplica todos los enteros del 1 a n. def factorialN")
print ("d)multiplica todos los enteros del 1 a n. def factorialNrecursiva")
print("2 ultimos incisos del 26 no entendi por el indentado")


