def restaurante(pizza):
    if pizza == 'si':
        return True
    elif pizza == 'no':
        return True
    else:
        return False


if __name__ == "__main__":
    pizza = input("¿Quieres una pizza vegetariana? (si/no): ")
    if pizza == 'si':
        print("Ingredientes de pizza vegetariana:\n1- Pimiento\n2- Tofu")
        ingrediente = input("De los ingredientes vegetarianos, ¿Qué desea ponerle a su pizza?: ")
        print("Su pizza será de mozzarella, tomate, ",ingrediente)
    elif pizza == 'no':
        print("Ingredientes de pizza no vegetariana:\n1- Peperoni\n2- Jamón\n3- Salmón")
        toping = input("De los ingredientes no vegetarianos, ¿Qué desea ponerle a su pizza?: ")
        print("Su pizza será de mozzarella, tomate, ",toping)
    