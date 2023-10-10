def empresa(puntuacion):
    if puntuacion == 0.0:
        return True
    elif puntuacion == 0.4:
        return True
    elif puntuacion >= 0.6:
        return True
    else:
        return False


if __name__ == "__main__":
    puntuacion = float(input("Escribe tu puntuación obtenida: "))
    dinero = puntuacion * 2400
    if empresa(puntuacion):
        if puntuacion == 0.0:
            print("Tu nivel de Rendimiento es 0.0 y el dinero conseguido es ",dinero)
        elif puntuacion == 0.4:
            print("Tu nivel de Rendimiento es 0.4 y el dinero conseguido es ", dinero)
        elif puntuacion >= 0.6:
            print("Tu nivel de Rendimiento es de 0.6 y el dinero conseguido es ",dinero)
        else:
            print("Error")
    else:
        print("Error")