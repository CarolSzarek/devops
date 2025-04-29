class Pet:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade
#last test
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.pets = []

    def adicionar_pet(self, pet):
        self.pets.append(pet)

    def remover_pet(self, nome_pet):
        self.pets = [pet for pet in self.pets if pet.nome != nome_pet]
