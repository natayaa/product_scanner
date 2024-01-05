from fastapi import FastAPI, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# load extended endpoint/api
# API
from api.user import User
from api.tv_model_api import product
from api.compare_data import scanner

# ENDPOINTS
from endpoint.index import index_page
from endpoint.logscan import logscan_page
from endpoint.product_data import product_page

app = FastAPI(title="Barcode Scanner", version="0.1.011")
app.mount("/static", StaticFiles(directory="templates/static"), name="static")
templates = Jinja2Templates(directory="templates/")

app.add_middleware(CORSMiddleware, allow_origins=["http://localhost"],
                   allow_credentials=True, allow_methods=["*"])


app.include_router(User)
app.include_router(product)
app.include_router(scanner)

# HTML Endpoints
app.include_router(index_page)
app.include_router(logscan_page)
app.include_router(product_page)