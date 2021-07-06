from src.tarea1 import contenidoFila

def test_contenido_filas():
    tablero = [ 
         [0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,],
         [0,0,0,0,0,0,0,],
         [2,1,1,2,2,1,1,],
         ] 

    assert [2,1,1,2,2,1,1,] == contenidoFila(6,tablero)