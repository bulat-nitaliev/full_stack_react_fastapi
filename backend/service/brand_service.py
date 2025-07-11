from dataclasses import dataclass
from repository.brand_repository import BrandRepository
from schemas.type_schema import TypeBrandSchema
from exception.store import TypeExistsException


@dataclass
class BrandService:
    brand_repo: BrandRepository

    async def create_brand(self, body) -> TypeBrandSchema:
        type_name = await self.brand_repo.get_brand_by_name(name=body.name)
        if type_name:
            raise TypeExistsException

        return await self.brand_repo.add_brand(body=body)

    async def get_brands(self):
        return await self.brand_repo.get_brands()

    async def get_brand_by_id(self, id: int):
        return await self.brand_repo.get_brand_by_id(id=id)
