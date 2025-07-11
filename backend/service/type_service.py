from dataclasses import dataclass
from repository.type_repository import TypeRepository
from schemas.type_schema import TypeBrandSchema
from exception.store import TypeExistsException


@dataclass
class TypeService:
    type_repo: TypeRepository

    async def create_type(self, body) -> TypeBrandSchema:
        type_name = await self.type_repo.get_type_by_name(name=body.name)
        if type_name:
            raise TypeExistsException

        return await self.type_repo.add_type(body=body)

    async def get_types(self):
        return await self.type_repo.get_types()
