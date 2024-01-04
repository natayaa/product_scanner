from pydantic import BaseModel

class CompareBody(BaseModel):
    tv_model: str 
    pic: str
    remote_tv_barcode: str
    