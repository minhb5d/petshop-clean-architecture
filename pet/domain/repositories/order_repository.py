from abc import ABC, abstractmethod
from domain.entities.order import Order

class OrderRepository(ABC):
    @abstractmethod
    def create_order(self, order: Order): pass

    @abstractmethod
    def list_orders(self): pass
