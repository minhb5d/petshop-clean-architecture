from domain.repositories.pet_repository import PetRepository

class ListPetsUseCase:
    def __init__(self, repo: PetRepository):
        self.repo = repo

    def execute(self):
        return self.repo.list_pets()
