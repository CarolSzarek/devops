import unittest
from petshop import Pet  # Supondo que a classe Pet esteja no arquivo petshop.py

class TestPetMethods(unittest.TestCase):
    
    def test_adicionar_pet(self):
        pet = Pet("Fido", "Cachorro")
        self.assertEqual(pet.nome, "Fido")
        self.assertEqual(pet.tipo, "Cachorro")
    
    def test_remover_pet(self):
        pet = Pet("Fido", "Cachorro")
        pet.remover()
        self.assertIsNone(pet.nome)
        self.assertIsNone(pet.tipo)

    def test_listar_pets(self):
        pet1 = Pet("Fido", "Cachorro")
        pet2 = Pet("Whiskers", "Gato")
        lista = [pet1, pet2]
        self.assertEqual(len(lista), 2)
        self.assertEqual(lista[0].nome, "Fido")
        self.assertEqual(lista[1].nome, "Whiskers")
