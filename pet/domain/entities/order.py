from pydantic import BaseModel

class Order(BaseModel):
    id: int
    pet_id: int
    customer_id: int
    status: str
