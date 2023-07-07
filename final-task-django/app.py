from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Cart(BaseModel):
    cart_id: int

class Order(BaseModel):
    order_id: int

class Item(BaseModel):
    item_id: int

@app.post("/cart")
def create_cart(cart: Cart):
    return {"message": "Cart created successfully"}


@app.get("/cart/{cart_id}")
def get_cart(cart_id: int):
    return {"cart_id": cart_id}


@app.put("/cart/{cart_id}")
def update_cart(cart_id: int, cart: Cart):
    return {"message": "Cart updated successfully"}


@app.delete("/cart/{cart_id}")
def delete_cart(cart_id: int):
    return {"message": "Cart deleted successfully"}


@app.post("/order")
def create_order(order: Order):
    return {"message": "Order created successfully"}


@app.get("/order/{order_id}")
def get_order(order_id: int):
    return {"order_id": order_id}


@app.put("/order/{order_id}")
def update_order(order_id: int, order: Order):
    return {"message": "Order updated successfully"}


@app.delete("/order/{order_id}")
def delete_order(order_id: int):
    return {"message": "Order deleted successfully"}


@app.post("/items")
def add_item(item: Item):
    return {"message": "Item added successfully"}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"message": "Item updated successfully"}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": "Item deleted successfully"}
