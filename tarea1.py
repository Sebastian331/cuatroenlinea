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
                        
secuencia =  [1,2,3,1]
dibujarTablero(completarTableroEnOrden(secuencia,tableroVacio()))
   