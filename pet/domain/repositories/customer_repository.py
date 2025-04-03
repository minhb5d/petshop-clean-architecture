from abc import ABC, abstractmethod
from domain.entities.customer import Customer

class CustomerRepository(ABC):
    @abstractmethod
    def add_customer(self, customer: Customer): pass

    @abstractmethod
    def get_customer_by_id(self, customer_id: int): pass
