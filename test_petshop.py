import unittest
from petshop import Pet, Cliente
#test
class TestPetshop(unittest.TestCase):

    def test_criar_pet(self):
        pet = Pet("Rex", "Cachorro", 5)
        self.assertEqual(pet.nome, "Rex")
        self.assertEqual(pet.especie, "Cachorro")  # Corrigido de tipo para especie
        self.assertEqual(pet.idade, 5)

    def test_idade_pet(self):
        pet = Pet("Miau", "Gato", 3)
        self.assertEqual(pet.idade, 3)

    def test_cliente_sem_pets(self):
        cliente = Cliente("Ana", "ana@email.com")  # Adicionado email
        self.assertEqual(len(cliente.pets), 0)

    def test_adicionar_pet(self):
        cliente = Cliente("João", "joao@email.com")  # Adicionado email
        pet = Pet("Toto", "Cachorro", 4)
        cliente.adicionar_pet(pet)
        self.assertEqual(len(cliente.pets), 1)
        self.assertEqual(cliente.pets[0].nome, "Toto")

    def test_remover_pet(self):
        cliente = Cliente("Maria", "maria@email.com")  # Adicionado email
        pet = Pet("Lulu", "Gato", 2)
        cliente.adicionar_pet(pet)
        cliente.remover_pet("Lulu")
        self.assertEqual(len(cliente.pets), 0)

if __name__ == "__main__":
    unittest.main()
