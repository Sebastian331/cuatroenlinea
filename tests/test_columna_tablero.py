from src.tarea1 import contenidocolumna

def test_contenido_columna():
    tablero = [ 
         [0,0,1,0,0,0,0,],
         [0,0,1,0,0,0,0,],
         [0,0,2,0,0,0,0,],
         [0,0,2,0,0,0,0,],
         [0,0,1,0,0,0,0,],
         [0,0,2,1,0,0,0,],
         ] 

    assert [1,1,2,2,1,2] == contenidocolumna(3,tablero)