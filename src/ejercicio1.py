def años(edad):
    if edad >= 18:
        return "Eres mayor de edad"
    else:
        return "Eres menor de edad"

if __name__ == "__main__":
    edad = int(input("¿Qué edad tienes?: "))
    print(años(edad))