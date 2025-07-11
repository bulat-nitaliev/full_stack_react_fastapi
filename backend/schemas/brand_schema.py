from pydantic import BaseModel


class CreateBrandSchema(BaseModel):
    name: str


class BrandSchema(CreateBrandSchema):
    id: int
