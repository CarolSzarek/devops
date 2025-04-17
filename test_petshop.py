from petshop import Cliente, Pet

def test_adicionar_pet():
    cliente = Cliente("Carlos")
    pet = Pet("Bob", "cachorro")
    cliente.adicionar_pet(pet)

    assert len(cliente.pets) == 1
    assert cliente.pets[0].nome == "Bob"
