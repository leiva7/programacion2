def crearMatrizCeros(filas,columnas):
    nombre = []
    for i in range(filas):
        nombre.append([])
        for j in range(columnas):
            nombre[i].append(0)
    return nombre

def cargarPorFila(filas,columnas):
    matriz = []
    a = 1
    n = filas * columnas
    while a < n:
        for i in range(filas):
            matriz.append([])
            for j in range(columnas):
                matriz[i].append(a)
                a +=1
    return matriz


def cargarPorColumna(filas,columnas):
    matriz = []
    n = filas*columnas
    a = 1
    while a < n:
        for i in range(filas):
            matriz.append([])
            for j in range(columnas):
                matriz[i].append(a)
                a +=filas
                if (j == columnas-1) and (i<(filas-1)) and (a!=n):
                    a = i+2
    return matriz  

def primo(x):
    contador = 0
    for num in range (1,x):
        if x%num == 0:
            contador +=1
    if contador == 1:
        return True
    else:
        return False