from domain.repositories.pet_repository import PetRepository
from domain.entities.pet import Pet

class PetRepositoryImpl(PetRepository):
    def __init__(self):
        self.pets = []

    def add_pet(self, pet: Pet):
        self.pets.append(pet)
        return pet

    def list_pets(self):
        return self.pets
