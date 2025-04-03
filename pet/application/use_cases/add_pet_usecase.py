from domain.entities.pet import Pet
from domain.repositories.pet_repository import PetRepository

class AddPetUseCase:
    def __init__(self, repo: PetRepository):
        self.repo = repo

    def execute(self, pet: Pet):
        return self.repo.add_pet(pet)
