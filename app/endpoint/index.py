from fastapi import APIRouter, status, HTTPException, Cookie, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

index_page = APIRouter(tags=['Homepage'])
template = Jinja2Templates(directory="templates/")

@index_page.get("/", response_class=HTMLResponse)
def index(request: Request):
    page_retval = {"request": request}
    return template.TemplateResponse("index.html", context=page_retval, status_code=status.HTTP_200_OK)