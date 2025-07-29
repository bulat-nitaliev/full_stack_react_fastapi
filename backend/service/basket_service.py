from dataclasses import dataclass
from schemas.basket_device_schema import BasketDeviceSchema
from repository.basket_repository import BasketRepository
from repository.device_repository import DeviceRepository
from exception.store import DeviceNotFoundException



@dataclass
class BasketService:
  basket_repo:BasketRepository
  device_repo:DeviceRepository

  async def add_device(self, device_id: int, user_id:int)->BasketDeviceSchema:
    device = await self.device_repo.get_device_by_device_id(device_id=device_id)
    print(device)
    if not device:
      raise DeviceNotFoundException
    return await self.basket_repo.create_device(
      device_id=device_id, 
      user_id=user_id
      )
  

  async def get_device(self, user_id:int)->BasketDeviceSchema:
    
    return await self.basket_repo.get_device(
      user_id=user_id
      )
  

  