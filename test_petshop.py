
    
   import unittest
from petshop import Cliente, Pet

class TestPetshop(unittest.TestCase):

    def test_criar_cliente(self):
        cliente = Cliente("João", "joao@email.com")
        self.assertEqual(cliente.nome, "João")
        self.assertEqual(cliente.email, "joao@email.com")

    def test_adicionar_pet(self):
        cliente = Cliente("Maria", "maria@email.com")
        pet = Pet("Rex", "Cachorro", 5)
        cliente.adicionar_pet(pet)
        self.assertIn(pet, cliente.pets)

    def test_listar_pets(self):
        cliente = Cliente("Pedro", "pedro@email.com")
        pet1 = Pet("Luna", "Gato", 3)
        pet2 = Pet("Thor", "Cachorro", 2)
        cliente.adicionar_pet(pet1)
        cliente.adicionar_pet(pet2)
        self.assertEqual(len(cliente.pets), 2)

    def test_remover_pet_existente(self):
        cliente = Cliente("Ana", "ana@email.com")
        pet = Pet("Bidu", "Cachorro", 4)
        cliente.adicionar_pet(pet)
        cliente.remover_pet("Bidu")
        self.assertEqual(len(cliente.pets), 0)

    def test_remover_pet_inexistente(self):
        cliente = Cliente("Carlos", "carlos@email.com")
        pet = Pet("Mimi", "Gato", 1)
        cliente.adicionar_pet(pet)
        cliente.remover_pet("Bob")
        self.assertEqual(len(cliente.pets), 1)  # Pet não removido porque não existe

if __name__ == '__main__':
    unittest.main()
