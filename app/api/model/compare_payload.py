from pydantic import BaseModel

class CompareBody(BaseModel):
    tv_model: str 
    tv_model_barcode: str
    pic: str
    remote_tv_barcode: str
    remote_name: str
    