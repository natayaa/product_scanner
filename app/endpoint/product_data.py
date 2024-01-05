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
@product_page.get("/products-page", response_class=HTMLResponse)
async def product_page_data(request: Request, search: str = None, limit: int = Query(10, alias="perpage"), offset: int = Query(1, alias="page")):
    # grab data from product_conn
    offsets = int((offset - 1) * limit)
    product_list = product_conn.product_show(search=search, limit=limit, offset=offsets)
    retval_page = {"request": request, "page": offsets, "limit": limit, "title": "Available Products",
                   "product_lists": product_list.get("product_list"), "total_records": product_list.get("total_products")}
    

    return template.TemplateResponse("product_page.html", context=retval_page, status_code=status.HTTP_200_OK)