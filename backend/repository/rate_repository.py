from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Rating
# from sqlalchemy import insert, select, join, desc
# from sqlalchemy.orm import selectinload, joinedload

@dataclass
class RateRepository:
  db_session: AsyncSession

  async def create_rate(self, rate:int, device_id: int, user_id:int)->Rating:
    async with self.db_session as session:
      rating = Rating(rate=rate, user_id=user_id, device_id=device_id)
      session.add(rating)
      await session.commit()
      await session.refresh(rating)

      return rating
