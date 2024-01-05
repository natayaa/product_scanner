from fastapi import APIRouter, status, HTTPException, Cookie, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# import customize lib
from database.product_connection import ProductConnection

product_page = APIRouter(tags=["Product Page"])
template = Jinja2Templates(directory="templates/")
# initialize ProductConnection
product_conn = ProductConnection()


# endpoint 
@product_page.get("/products-page")
async def product_page_data(request: Request, search: str = None, limit: int = Query(10, alias="pages"), offset: int = Query(0, alias="perpage")):
    # grab data from product_conn
    product_list = product_conn.product_show(search=search, limit=limit, offset=offset)
    retval_page = {"request": request, "product_lists": product_list.get("product_list"), "total_records": product_list.get("total_products")}

    return template.TemplateResponse("product_page.html", context=retval_page, status_code=status.HTTP_200_OK)