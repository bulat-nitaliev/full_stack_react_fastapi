from service.brand_service import BrandService
from service.device_service import DeviceService
from repository.device_repository import DeviceRepository
from repository.brand_repository import BrandRepository
from repository.user_repository import UserRepository
from repository.type_repository import TypeRepository
from service.user_service import UserService
from service.auth_service import AuthService
from service.type_service import TypeService
from settings.config import Settings
from db import helper
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends


async def get_db_session():
    async with helper.session_factory() as session:
        yield session


def get_user_repository(db_session: AsyncSession = Depends(get_db_session)):

    return UserRepository(db_session=db_session)


def get_user_service(
    user_repo: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(user_repo=user_repo)


def get_auth_service(
    user_repo: UserRepository = Depends(get_user_repository),
) -> AuthService:
    return AuthService(user_repo=user_repo, settings=Settings())


def get_type_repository(db_session: AsyncSession = Depends(get_db_session)):
    return TypeRepository(db_session=db_session)


def get_type_service(
    type_repo: TypeRepository = Depends(get_type_repository),
) -> TypeService:
    return TypeService(type_repo=type_repo)


def get_brand_repository(db_session: AsyncSession = Depends(get_db_session)):
    return BrandRepository(db_session=db_session)


def get_brand_service(
    brand_repo: TypeRepository = Depends(get_brand_repository),
) -> BrandService:
    return BrandService(brand_repo=brand_repo)


def get_device_repository(db_session: AsyncSession = Depends(get_db_session)):
    return DeviceRepository(db_session=db_session)


def get_device_service(
    device_repo: DeviceRepository = Depends(get_device_repository),
) -> DeviceService:
    return DeviceService(device_repo=device_repo)
