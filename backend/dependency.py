from service.brand_service import BrandService
from service.device_service import DeviceService
from repository.device_repository import DeviceRepository
from repository.brand_repository import BrandRepository
from repository.user_repository import UserRepository
from repository.type_repository import TypeRepository
from repository.rate_repository import RateRepository
from repository.basket_repository import BasketRepository
from service.basket_service import BasketService
from service.rate_service import RateService
from service.user_service import UserService
from service.auth_service import AuthService
from service.type_service import TypeService
from settings.config import Settings
from db import helper
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Request, security, Security, HTTPException, status
from exception.token import TokenException


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


def get_rating_repository(db_session: AsyncSession = Depends(get_db_session)):
    return RateRepository(db_session=db_session)


def get_rating_service(
    rate_repo: RateRepository = Depends(get_rating_repository),
    device_repo: DeviceRepository = Depends(get_device_repository),
) -> RateService:
    return RateService(rate_repo=rate_repo, device_repo=device_repo)


def get_basket_repository(db_session: AsyncSession = Depends(get_db_session)):
    return BasketRepository(db_session=db_session)


def get_basket_service(
    basket_repo: BasketRepository = Depends(get_basket_repository),
    device_repo: DeviceRepository = Depends(get_device_repository),
) -> RateService:
    return BasketService(
        basket_repo=basket_repo,
        device_repo=device_repo
        )



reuseable_oauth = security.HTTPBearer()


async def get_request_user_id(
    request: Request,
    token: security.http.HTTPAuthorizationCredentials = Security(reuseable_oauth),
    auth_service: AuthService = Depends(get_auth_service),
):
    try:
        user_id = auth_service.get_user_id_from_access_token(token.credentials)
       
    except TokenException as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e.detail)
    return user_id


async def get_request_role(
    request: Request,
    token: security.http.HTTPAuthorizationCredentials = Security(reuseable_oauth),
    auth_service: AuthService = Depends(get_auth_service),
):
    try:
        role = auth_service.get_role_from_access_token(token.credentials)
       
    except TokenException as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e.detail)
    return role