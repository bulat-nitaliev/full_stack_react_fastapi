from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str
    # role:str


class UserSchema(BaseModel):
    id: int
    email: EmailStr
    name: str
