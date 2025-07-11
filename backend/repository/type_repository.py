from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.type_schema import TypeBrandSchema, CreateTypeBrandSchema
from db.models import Type
from sqlalchemy import select, insert


@dataclass
class TypeRepository:
    db_session: AsyncSession

    async def add_type(self, body: CreateTypeBrandSchema):
        async with self.db_session as session:
            query = (
                insert(Type)
                .values(
                    name=body.name,
                )
                .returning(Type.id)
            )
            type_id: int = await session.execute(query)

            await session.commit()
            return await self.get_type_by_id(id=type_id.scalar())

    async def get_types(self) -> list[TypeBrandSchema]:
        async with self.db_session as session:
            query = select(Type).order_by("id")
            res = await session.execute(query)
            return list(res.scalars().all())

    async def get_type_by_id(self, id: int) -> Type:
        async with self.db_session as session:
            query = select(Type).where(Type.id == id)
            res = await session.execute(query)
            return res.scalar()

    async def get_type_by_name(self, name: str) -> Type:
        async with self.db_session as session:
            query = select(Type).where(Type.name == name)
            res = await session.execute(query)
            return res.scalar()
