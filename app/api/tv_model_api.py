from fastapi import APIRouter, status, Request, HTTPException, Cookie
from fastapi.responses import Response, JSONResponse

# load database
from database.product_connection import ProductConnection
# load register item model schema
from api.model.product import RegisterProduct

pconnect = ProductConnection()

product = APIRouter(tags=['API Products'], prefix="/app/resources/api/v1/data")

@product.get("/products", response_class=JSONResponse)
async def listing_products(response: Response):
    products = await pconnect.listing_model()
    tv_model_list = [{'tv_model': model, 'tv_barcode': barcode} for model, barcode in products]
    return JSONResponse(content={"tv_model_list": tv_model_list}, status_code=status.HTTP_200_OK)

@product.post("/products/add_product", response_class=JSONResponse)
def add_tv_product(register_payload: RegisterProduct):
    detail = {"tv_model": register_payload.tv_model,
              "tv_barcode": register_payload.tv_barcode, "remote_name": register_payload.remote_name,
              "remote_barcode": register_payload.remote_barcode}
    register_product = pconnect.add_product(username=register_payload.insert_by, **detail)
    if register_product:
        return JSONResponse(content={"message": "Data has been inputted into database."}, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"message": "Something went wrong"}, status_code=status.HTTP_400_BAD_REQUEST)