from src.ejercicio6 import grupos

def test_grupos():
    nombre = 'alberto'
    sexo = 'm'
    assert grupos(nombre,sexo) == True