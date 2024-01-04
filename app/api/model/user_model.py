from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    password: str
    role: str 
    level: int = 100
    
class ResponseUser(BaseModel):
    message: str
    status: str
    success: bool
    
