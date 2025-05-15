from pydantic import BaseModel
from pydantic import EmailStr


class LoginSchema(BaseModel):
    user_id:int
    access_token:str

class Login(BaseModel):
    email:EmailStr
    password:str