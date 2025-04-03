from fastapi import APIRouter
from domain.entities.customer import Customer
from infrastructure.database.customer_repository_impl import CustomerRepositoryImpl

router = APIRouter()
repo = CustomerRepositoryImpl()

@router.post("/customers")
def add_customer(customer: Customer):
    return repo.add_customer(customer)

@router.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    return repo.get_customer_by_id(customer_id)
