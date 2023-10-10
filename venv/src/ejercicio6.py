def grupos(nombre,sexo):
    if (sexo == 'm' and nombre.lower() < 'm') or (sexo == 'h' and nombre.lower() > 'n'):
        if nombre.lower() < 'm':
            return True
        else:
            return False

if __name__ == "__main__":
    nombre = input("¿Como te llamas?: ")
    sexo = input("¿Cuál es tu sexo?(M o F): ")
    if grupos(nombre,sexo):
        print("Perteneces al grupo A")
    else:
        print("Perteneces al grupo B")