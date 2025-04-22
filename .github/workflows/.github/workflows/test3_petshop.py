import unittest
from petshop import Pet, Cliente  # certifique-se que o nome do seu arquivo com as classes seja petshop.py

class TestPetShop(unittest.TestCase):
    def test_criacao_pet(self):
        pet = Pet("Fido", "cachorro")
        self.assertEqual(pet.nome, "Fido")
        self.assertEqual(pet.especie, "cachorro")

    def test_repr_pet(self):
        pet = Pet("Luna", "gato")
        self.assertEqual(str(pet), "Luna é um(a) gato")

    def test_adicionar_pet(self):
        cliente = Cliente("Ana")
        pet = Pet("Bolt", "cachorro")
        cliente.adicionar_pet(pet)
        self.assertIn(pet, cliente.pets)

    def test_remover_pet(self):
        cliente = Cliente("Pedro")
        pet1 = Pet("Nina", "gata")
        pet2 = Pet("Thor", "cachorro")
        cliente.adicionar_pet(pet1)
        cliente.adicionar_pet(pet2)
        cliente.remover_pet("Nina")
        self.assertNotIn(pet1, cliente.pets)

    def test_listar_pets(self):
        cliente = Cliente("Maria")
        pet1 = Pet("Rex", "cachorro")
        pet2 = Pet("Mimi", "gata")
        cliente.adicionar_pet(pet1)
        cliente.adicionar_pet(pet2)
        self.assertEqual(cliente.listar_pets(), ["Rex é um(a) cachorro", "Mimi é um(a) gata"])

if __name__ == '__main__':
    unittest.main()
