def renta_anual(renta):
    if renta < 10000:
        return True
    elif renta < 20000:
        return True
    elif renta < 35000:
        return True
    elif renta < 60000:
        return True
    else:
        return False


if __name__ == "__main__":
    renta = float(input("Escribe tu renta anual: "))
    if renta < 10000:
        print("Tienes un tipo impositivo del 5%")
    elif renta < 20000:
        print("Tienes un tipo impositivo del 15%")
    elif renta < 35000:
        print("Tienes un tipo impositivo del 20%")
    elif renta < 60000:
        print("Tienes un tipo impositivo del 30%")
    else:
        print("Tienes un tipo impositivo del 45%")
    