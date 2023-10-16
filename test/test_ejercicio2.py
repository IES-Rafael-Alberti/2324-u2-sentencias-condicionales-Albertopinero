from src.ejercicio2 import seguridad

def test_seguridad():
    privado = 'cOnTrAsEñA'
    assert seguridad(privado) == 'La contraseña es correcta'