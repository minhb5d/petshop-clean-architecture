from fastapi import APIRouter
from domain.entities.order import Order
from infrastructure.database.order_repository_impl import OrderRepositoryImpl

router = APIRouter()
repo = OrderRepositoryImpl()

@router.post("/orders")
def create_order(order: Order):
    return repo.create_order(order)

@router.get("/orders")
def list_orders():
    return repo.list_orders()
