from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.type_schema import TypeBrandSchema, CreateTypeBrandSchema
from db.models import Brand
from sqlalchemy import select, insert


@dataclass
class BrandRepository:
    db_session: AsyncSession

    async def add_brand(self, body: CreateTypeBrandSchema):
        async with self.db_session as session:
            query = (
                insert(Brand)
                .values(
                    name=body.name,
                )
                .returning(Brand.id)
            )
            type_id: int = await session.execute(query)

            await session.commit()
            return await self.get_brand_by_id(id=type_id.scalar())

    async def get_brands(self) -> list[TypeBrandSchema]:
        async with self.db_session as session:
            query = select(Brand).order_by("id")
            res = await session.execute(query)
            return list(res.scalars().all())

    async def get_brand_by_id(self, id: int) -> Brand:
        async with self.db_session as session:
            query = select(Brand).where(Brand.id == id)
            res = await session.execute(query)
            return res.scalar()

    async def get_brand_by_name(self, name: str) -> Brand:
        async with self.db_session as session:
            query = select(Brand).where(Brand.name == name)
            res = await session.execute(query)
            return res.scalar()
