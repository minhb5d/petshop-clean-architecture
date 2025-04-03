from domain.repositories.customer_repository import CustomerRepository
from domain.entities.customer import Customer

class CustomerRepositoryImpl(CustomerRepository):
    def __init__(self):
        self.customers = []

    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        return customer

    def get_customer_by_id(self, customer_id: int):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None
