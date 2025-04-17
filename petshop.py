class Pet:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def __str__(self):
        return f"{self.nome} é um(a) {self.especie}"


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.pets = []

    def adicionar_pet(self, pet):
        self.pets.append(pet)
    def remover_pet(self, nome_pet):
        self.pets = [pet for pet in self.pets if pet.nome != nome_pet]

    def listar_pets(self):
        return [str(pet) for pet in self.pets]
