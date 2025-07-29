from pydantic import BaseModel


class RatingSchema(BaseModel):
  rate: int
  device_id: int