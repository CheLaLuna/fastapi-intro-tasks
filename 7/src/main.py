from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)

@app.post("/product")
async def create_product(product: Product):
    global product_id_counter
    product_data = product.dict()
    product_data["id"] = product_id_counter
    product_list.append(product_data)
    product_id_counter += 1
    return {"message": "Product added successfully", "product": product_data}

@app.get("/products", response_model=List[Product])
async def get_products():
    return {"products": product_list}
# END
