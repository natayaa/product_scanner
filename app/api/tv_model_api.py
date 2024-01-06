from fastapi import APIRouter, status, Request, HTTPException, Cookie
from fastapi.responses import Response, JSONResponse

# load database
from database.product_connection import ProductConnection
# load register item model schema
from api.model.product import RegisterProduct

pconnect = ProductConnection()

product = APIRouter(tags=['API Products'], prefix="/app/resources/api/v1/data")

# listing products
@product.get("/products", response_class=JSONResponse)
async def listing_products(response: Response):
    products = await pconnect.listing_model()
    tv_model_list = [{'tv_model': model, 'tv_barcode': barcode, 'carton_barcode': carton_barcode} for model, barcode, carton_barcode in products]
    return JSONResponse(content={"tv_model_list": tv_model_list, "status_code": status.HTTP_200_OK}, status_code=status.HTTP_200_OK)

# adding product api
@product.post("/products/add_product", response_class=JSONResponse)
def add_tv_product(register_payload: RegisterProduct):
    detail = {"tv_model": register_payload.tv_model,
              "carton_barcode": register_payload.carton_barcode,
              "remote_barcode": register_payload.remote_barcode}
    register_product = pconnect.add_product(username=register_payload.insert_by, **detail)
    if register_product:
        return JSONResponse(content={"message": "Data has been inputted into database.", "status_code": status.HTTP_201_CREATED}, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(content={"message": "Something went wrong", "status_code": status.HTTP_400_BAD_REQUEST}, status_code=status.HTTP_400_BAD_REQUEST)
    
@product.delete("/products/delete", response_class=JSONResponse)
def delete_registered_product(item_id: int):
    delete_product = pconnect.delete_product(item_id=item_id)
    return JSONResponse(content={"message": f"{delete_product} has been deleted."})