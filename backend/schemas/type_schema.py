from pydantic import BaseModel


class CreateTypeBrandSchema(BaseModel):
    name: str


class TypeBrandSchema(CreateTypeBrandSchema):
    id: int
