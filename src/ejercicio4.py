def espar(num1):
    if num1 % 2 == 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    num1 = int(input("Escribe un número: "))
    if espar(num1):
        print("Es par")
    else:
        print("Es impar")