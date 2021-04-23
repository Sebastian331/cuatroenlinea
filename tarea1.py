def tableroVacio():
    return [ 
         [0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,],
         ] 

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

if SecuenciaCorrecta(secuencia):
    dibujarTablero(completarTableroEnOrden(secuencia,tableroVacio()))
else:
     print("Las columnas estan compredidas entre el 1 y el 7")  