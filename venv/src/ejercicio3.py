def division(num2):
    if num2 == 0:
        return True
    else: 
        return False

if __name__ == "__main__":
    num1 = int(input("Escribe el primer número: "))
    num2 = int(input("Escribe el segundo número: "))
    if division(num2):
        print("Error")
    else:
        dividir = num1 / num2
        print("EL resultado es ", dividir)