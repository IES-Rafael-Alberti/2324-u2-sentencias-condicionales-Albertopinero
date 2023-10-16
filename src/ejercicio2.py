def seguridad(privado):
    password = 'contraseña'
    if password == privado.lower():
        return "La contraseña es correcta"
    else:
        return "Contraseña Incorrecta"
    
if __name__ == "__main__":
    privado = input("Escribe tu contraseña: ")
    print(seguridad(privado))