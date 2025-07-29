from pydantic import BaseModel


class BasketDeviceSchema(BaseModel):
  device_id: int