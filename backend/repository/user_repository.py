from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user_schema import UserCreate, UserSchema
from db.models import User , Basket
from sqlalchemy import select, insert


@dataclass
class UserRepository:
    db_session: AsyncSession

    async def add_user(self, body: UserCreate):
        async with self.db_session as session:
            query = (
                insert(User)
                .values(email=body.email, name=body.name, password=body.password)
                .returning(User.id)
            )
            user_id: int = (await session.execute(query)).scalar()
            
            await session.execute(insert(Basket).values(user_id=user_id))

            await session.commit()
            return await self.get_user_by_id(id=user_id)

    async def get_users(self) -> list[UserSchema]:
        async with self.db_session as session:
            query = select(User).order_by("id")
            res = await session.execute(query)
            return list(res.scalars().all())

    async def get_user_by_id(self, id: int) -> User:
        async with self.db_session as session:
            query = select(User).where(User.id == id)
            res = await session.execute(query)
            return res.scalar()

    async def get_user_by_email(self, email: str) -> User:
        async with self.db_session as session:
            query = select(User).where(User.email == email)
            res = await session.execute(query)
            return res.scalar()
