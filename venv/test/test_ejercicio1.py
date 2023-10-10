from src.ejercicio1 import años

def test_años():
    edad = 18
    assert años(edad) == 'Eres mayor de edad'