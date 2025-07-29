from dataclasses import dataclass
from schemas.rating import RatingSchema
from repository.rate_repository import RateRepository
from repository.device_repository import DeviceRepository
from exception.store import DeviceNotFoundException


@dataclass
class RateService:
  rate_repo:RateRepository
  device_repo:DeviceRepository

  async def add_rate(self, rate:int, device_id: int, user_id:int)->RatingSchema:
    device = await self.device_repo.get_device_by_device_id(device_id=device_id)
    print(device)
    if not device:
      raise DeviceNotFoundException
    return await self.rate_repo.create_rate(
      rate=rate, 
      device_id=device_id, 
      user_id=user_id
      )