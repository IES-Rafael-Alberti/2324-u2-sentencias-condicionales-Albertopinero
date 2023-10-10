def tributar(edad,ingresos):
    if edad > 16 and ingresos >= 1000:
        return True
    else:
        return False

if __name__ == "__main__":
    edad = int(input("Escribe tu edad: "))
    ingresos = int(input("Escribe tus ingresos mensuales: "))
    if tributar(edad,ingresos):
        print("Tiene que tributar")
    else:
        print("No tiene que tributar")
