def salas(edad):
    if edad < 4:
        return True
    elif edad <= 18:
        return True
    elif edad > 18:
        return True
    else: 
        return False

if __name__ == "__main__":
    edad = int(input("Ecribe tu edad: "))
    if edad < 4:
        print("Entras gratis")
    elif edad <= 18:
        print("El precio es de 5€")
    elif edad > 18:
        print("Tienes que pagar 10€")
    else: 
        print("Error")