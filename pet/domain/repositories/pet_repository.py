from abc import ABC, abstractmethod
from domain.entities.pet import Pet

class PetRepository(ABC):
    @abstractmethod
    def add_pet(self, pet: Pet): pass

    @abstractmethod
    def list_pets(self): pass
