def factorial(n):
    if n==1:
        return 1
    else:
        return n*(n-1)
    
print (factorial(1000))

def potencia(x,n):
    if n==0:
        return 1
    else:
        return x*x*(n-1)
print(potencia(3,2))