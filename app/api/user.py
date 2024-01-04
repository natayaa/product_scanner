from fastapi import APIRouter, status, Request, Cookie, HTTPException
from fastapi.responses import JSONResponse, Response
from decouple import config

from database.user_connection import UserConnection
# load the user model
from api.model.user_model import UserSchema, ResponseUser

user_conn = UserConnection()

User = APIRouter(tags=["User Management"], prefix="/app/endpoint/api/v1/user")

# register user
@User.post("/register", response_model=ResponseUser, response_class=JSONResponse)
async def insert_user(response: Response, user_schema: UserSchema):
    user_handler = {"username": user_schema.username, "password": user_schema.password,
                    "role": user_schema.role}
    register_user = user_conn.register_user(**user_handler)
    if register_user:
        return {"message": "OK", "status": status.HTTP_201_CREATED, "success": register_user}
    else:
        return {"message": "NG", "status": status.HTTP_400_BAD_REQUEST, "success": register_user}
    
# DELETE USER 
@User.post("/delete", response_model=ResponseUser, response_class=JSONResponse)
def delete_user(response: Response, user_id: int):
    del_usr = user_conn.delete_user(user_id=user_id)
    if delete_user:
        return {"message": "Account has been deleted.", "status": status.HTTP_202_ACCEPTED, "success": del_usr}
    else:
        return {"message": "Failed, something went wrong", "status": status.HTTP_400_BAD_REQUEST, "success": del_usr}
    