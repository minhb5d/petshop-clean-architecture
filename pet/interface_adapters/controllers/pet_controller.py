from fastapi import APIRouter
from domain.entities.pet import Pet
from application.use_cases.add_pet_usecase import AddPetUseCase
from application.use_cases.list_pets_usecase import ListPetsUseCase
from infrastructure.database.pet_repository_impl import PetRepositoryImpl

router = APIRouter()
repo = PetRepositoryImpl()
add_usecase = AddPetUseCase(repo)
list_usecase = ListPetsUseCase(repo)

@router.post("/pets")
def add_pet(pet: Pet):
    return add_usecase.execute(pet)

@router.get("/pets")
def list_pets():
    return list_usecase.execute()
