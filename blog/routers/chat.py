from fastapi import APIRouter
from blog import schemas
from blog.utils import generate_description
from blog.schemas import Product
import requests

router = APIRouter(
    prefix='/chat',
    tags=['Chats']
)

# @router.get("/hello")
# async def hello_endpoint(name: str = 'World'):
#     return {"message": f"Hello, {name}!"}

# @router.post("/orders")
# async def place_order(product: str, units: int):
#     url = 'http://127.0.0.1:8000/orders'
#     headers = {
#         'accept': 'application/json',
#     }
#     params = {
#         'product': 'laptop',
#         'units': '1'
#     }

#     response = requests.post(url, headers=headers, params=params)

#     print(response.json())
#     return {"message": f"Order for {units} units of {product} placed successfully."}

@router.post("/orders_pydantic")
async def place_order(order: schemas.Order):
    return {"message": f"Order for {order.units} units of {order.product} placed successfully."}

@router.post("/product_description")
async def generate_product_description(product: Product):
    description = generate_description(f"Product name: {product.name}, Notes: {product.notes}")
    return {"product_description": description}