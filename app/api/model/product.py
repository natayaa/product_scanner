from pydantic import BaseModel

class RegisterProduct(BaseModel):
    tv_model: str
    tv_barcode: str
    remote_name: str
    remote_barcode: str
    insert_by: str
    