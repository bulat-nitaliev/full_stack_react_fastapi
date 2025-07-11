from pydantic import BaseModel


class DeviceInfoCreate(BaseModel):
    title: str
    description: str


class DeviceSchema(BaseModel):
    id: int
    name: str
    price: int
    rating: float
    img: str
    type_id: int
    brand_id: int
    


class ListDeviceSchema(DeviceSchema):
    title:str
    description:str 
