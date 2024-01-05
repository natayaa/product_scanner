from pydantic import BaseModel

class CompareBody(BaseModel):
    tv_model: str 
    scanner_line: str
    pic: str
    remote_tv_barcode: str
    carton_barcode: str
    