
import unittest

# Exemplo de classes para o código de teste
class Pet:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def validar(self):
        if not self.nome or not self.especie or self.idade <= 0:
            return False
        return True


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.pets = []

    def adicionar_pet(self, pet):
        if pet.validar():
            self.pets.append(pet)

    def remover_pet(self, pet):
        if pet in self.pets:
            self.pets.remove(pet)

    def listar_pets(self):
        return self.pets


class TestPetshop(unittest.TestCase):
    
    def test_adicionar_pet(self):
        cliente = Cliente("Carlos")
        pet = Pet("Fido", "Cachorro", 2)
        cliente.adicionar_pet(pet)
        self.assertIn(pet, cliente.pets, "Pet não foi adicionado corretamente.")
    
    def test_remover_pet(self):
        cliente = Cliente("Carlos")
        pet = Pet("Fido", "Cachorro", 2)
        cliente.adicionar_pet(pet)
        cliente.remover_pet(pet)
        self.assertNotIn(pet, cliente.pets, "Pet não foi removido corretamente.")
    
    def test_listar_pets(self):
        cliente = Cliente("Carlos")
        pet1 = Pet("Fido", "Cachorro", 2)
        pet2 = Pet("Miau", "Gato", 1)
        cliente.adicionar_pet(pet1)
        cliente.adicionar_pet(pet2)
        pets = cliente.listar_pets()
        self.assertEqual(pets, [pet1, pet2], "A lista de pets não está correta.")
    
    def test_validar_pet(self):
        pet = Pet("Fido", "Cachorro", 2)
        self.assertTrue(pet.validar(), "Pet válido não foi validado corretamente.")
    
    def test_cliente_sem_pets(self):
        cliente = Cliente("Carlos")
        self.assertEqual(cliente.listar_pets(), [], "Cliente não tem pets, mas a lista não está vazia.")
        
if __name__ == '__main__':
    unittest.main()
