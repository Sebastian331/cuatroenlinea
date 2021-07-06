from src.tarea1 import SecuenciaCorrecta

def test_secuencia_correcta():
    secuencia = [1,2,1,3,4,5,6,7,3]

    assert SecuenciaCorrecta(secuencia) == True