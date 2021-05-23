def tableroVacio():
    return [ 
         [0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,],
         ] 

def contenidocolumna(nro_columna, tablero):
    colunma = []
    for fila in tablero:
        celda = fila [nro_columna - 1]
        colunma.append(celda)
    return colunma

def contenidoFila(nro_fila, tablero):
    fila = []
    for celda in tablero [nro_fila - 1]:
        fila.append(celda)
    return fila

def todasColumas(tablero):
    colum_array = []
    col = []
    for columna in range(7):
        for fila in tablero:
            celda = fila[columna]
            col.append(celda)
        colum_array.append(col)
        col = []
    return colum_array

def todasFilas(tablero):
    fil_array = []
    for fila in tablero:
        fil_array.append(fila)
    return fil_array

def completarTableroEnOrden(secuencia, tablero):
    j=0
    for elemento in secuencia:
        if j%2 == 0:
            soltarFichaEnColumna(1,elemento,tablero)
        else:
           soltarFichaEnColumna(2,elemento,tablero)
        j+=1
    return tablero

def soltarFichaEnColumna(ficha,columna,tablero):
    for fila in range(6, 0, -1):
        if tablero [fila - 1] [columna - 1] == 0:
            tablero [fila - 1] [columna - 1] = ficha
            return

def dibujarTablero(tablero):
    for x in tablero:
        print(x)

def SecuenciaCorrecta(secuencia):
    for columna in secuencia:
        if columna < 1 or columna > 7:
            return False
    return True

secuencia =  [1,2,3,1,3,4]

tablero = []
if SecuenciaCorrecta(secuencia):
    tablero = completarTableroEnOrden(secuencia,tableroVacio())
    dibujarTablero(tablero)
else:
     print("Las columnas estan compredidas entre el 1 y el 7")  

print(contenidocolumna(1,tablero))
print(contenidoFila(6,tablero))
print(todasColumas(tablero))
print(todasFilas(tablero))