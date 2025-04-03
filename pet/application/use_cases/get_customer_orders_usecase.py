from domain.repositories.order_repository import OrderRepository

class GetCustomerOrdersUseCase:
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    def execute(self, customer_id: int):
        return [order for order in self.repo.list_orders() if order.customer_id == customer_id]
