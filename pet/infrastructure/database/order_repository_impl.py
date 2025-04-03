from domain.repositories.order_repository import OrderRepository
from domain.entities.order import Order

class OrderRepositoryImpl(OrderRepository):
    def __init__(self):
        self.orders = []

    def create_order(self, order: Order):
        self.orders.append(order)
        return order

    def list_orders(self):
        return self.orders
