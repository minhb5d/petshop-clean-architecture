from domain.entities.order import Order
from domain.repositories.order_repository import OrderRepository

class CreateOrderUseCase:
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    def execute(self, order: Order):
        return self.repo.create_order(order)
