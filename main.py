from petshop import Cliente, Pet

def main():
    cliente = Cliente("Ana")
    pet1 = Pet("Rex", "cachorro")
    pet2 = Pet("Mimi", "gato")

    cliente.adicionar_pet(pet1)
    cliente.adicionar_pet(pet2)

    print(f"Cliente: {cliente.nome}")
    print("Pets cadastrados:")
    for pet in cliente.listar_pets():
        print("-", pet)

if __name__ == "__main__":
    main()
