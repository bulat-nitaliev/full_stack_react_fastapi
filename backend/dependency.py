from users.userprofile.repository import UserRepository
from users.userprofile.service import UserService
from users.auth.service import AuthService
from settings.config import Settings
from db import helper
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

async def get_db_session():
    async with helper.session_factory() as session:
        yield session


def get_user_repository(db_session: AsyncSession = Depends(get_db_session)):
    
    return UserRepository(db_session=db_session)


def get_user_service(user_repo:UserRepository = Depends(get_user_repository))->UserService:
    return UserService(user_repo=user_repo)


def get_auth_service(user_repo:UserRepository = Depends(get_user_repository))->AuthService:
    return AuthService(user_repo=user_repo, settings=Settings())