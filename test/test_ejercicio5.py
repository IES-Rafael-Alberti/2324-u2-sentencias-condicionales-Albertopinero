from src.ejercicio5 import tributar

def test_tributar():
    edad = 17
    ingresos = 1000
    assert tributar(edad,ingresos) == True