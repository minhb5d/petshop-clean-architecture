from fastapi import FastAPI
from interface_adapters.controllers import pet_controller, customer_controller, order_controller

app = FastAPI()

app.include_router(pet_controller.router)
app.include_router(customer_controller.router)
app.include_router(order_controller.router)

@app.get("/")
def root():
    return {"message": "Chào mừng đến với cửa hàng thú cưng"}
