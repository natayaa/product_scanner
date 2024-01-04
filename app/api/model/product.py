from pydantic import BaseModel

class RegisterProduct(BaseModel):
    tv_model: str
    remote_barcode: str
    insert_by: str
    