from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Basket, BasketDevice
from sqlalchemy import insert, select, join, desc
# from sqlalchemy.orm import selectinload, joinedload

@dataclass
class BasketRepository:
  db_session: AsyncSession

  async def create_device(self, device_id: int, user_id:int)->BasketDevice:
    async with self.db_session as session:
      basket_id = await self.get_basket_by_user_id(user_id=user_id)
      basket = BasketDevice(basket_id=basket_id, device_id=device_id)
      session.add(basket)
      await session.commit()
      await session.refresh(basket)

      return basket
    

  async def get_basket_by_user_id(self, user_id:int)->int:
    async with self.db_session as session:
      stmt = select(Basket).where(Basket.user_id==user_id)
      basket_id = await session.execute(stmt)
      print(basket_id)
      return basket_id.scalar().id
    

  async def get_device(self, user_id:int):
    async with self.db_session as session:
      basket_id = await self.get_basket_by_user_id(user_id=user_id)
      stmt = select(BasketDevice).where(BasketDevice.basket_id==basket_id)
      res = await session.execute(stmt)
      return res.scalars().all()
