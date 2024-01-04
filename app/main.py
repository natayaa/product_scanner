from fastapi import FastAPI, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# load extended endpoint/api
# API
from api.user import User

# ENDPOINTS
from endpoint.index import index_page

app = FastAPI(title="Barcode Scanner", version="0.1.011")
app.mount("/static", StaticFiles(directory="templates/static"), name="static")
templates = Jinja2Templates(directory="templates/")

app.add_middleware(CORSMiddleware, allow_origins=["http://localhost"],
                   allow_credentials=True, allow_methods=["*"])

app.include_router(User)
app.include_router(index_page)