import unittest
from petshop import Pet, Cliente  # substitua 'petshop' pelo nome do seu arquivo Python

class TestPetshop(unittest.TestCase):

    def test_pet_criacao(self):
        pet = Pet("Rex", "cachorro")
        self.assertEqual(pet.nome, "Rex")
        self.assertEqual(pet.especie, "cachorro")

    def test_pet_str(self):
        pet = Pet("Luna", "gato")
        self.assertEqual(str(pet), "Luna é um(a) gato")

    def test_cliente_criacao(self):
        cliente = Cliente("João")
        self.assertEqual(cliente.nome, "João")
        self.assertEqual(cliente.pets, [])

    def test_adicionar_pet(self):
        cliente = Cliente("João")
        pet = Pet("Rex", "cachorro")
        cliente.adicionar_pet(pet)
        self.assertEqual(len(cliente.pets), 1)

    def test_remover_pet(self):
        cliente = Cliente("João")
        pet1 = Pet("Rex", "cachorro")
        pet2 = Pet("Luna", "gato")
        cliente.adicionar_pet(pet1)
        cliente.adicionar_pet(pet2)
        cliente.remover_pet("Rex")
        self.assertEqual(len(cliente.pets), 1)
        self.assertEqual(cliente.pets[0].nome, "Luna")

    def test_listar_pets(self):
        cliente = Cliente("João")
        pet = Pet("Rex", "cachorro")
        cliente.adicionar_pet(pet)
        self.assertEqual(cliente.listar_pets(), ["Rex é um(a) cachorro"])

if __name__ == '__main__':
    unittest.main()
