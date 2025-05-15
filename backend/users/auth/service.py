
from users.userprofile.repository import UserRepository
from dataclasses import dataclass
from .schema import LoginSchema
from users.userprofile.model import UserProfile
from exception.user import UserNotCorrectPasswordException, UserNotFoundException
from settings.config import Settings
from jose import jwt, JWTError
from datetime import datetime, timedelta, UTC


@dataclass
class AuthService:
    user_repo:UserRepository
    settings:Settings


    async def login(self,email:str, password:str)->LoginSchema:
        user = await self.user_repo.get_user_by_email(email=email)
        self.validate(user=user, password=password)
        access_token = self.create_access_token(user_id=user.id)

        return LoginSchema(user_id=user.id, access_token=access_token)


    @staticmethod
    def validate(user:UserProfile, password:str):
        if not user:
            raise UserNotFoundException
        if user.password != password:
            raise UserNotCorrectPasswordException
        
    def create_access_token(self,user_id:int):
        dt_expire = (datetime.now(tz=UTC) + timedelta(days=7)).timestamp()
        token = jwt.encode(
            {"user_id": user_id, "exp": dt_expire},
            key=self.settings.JWT_SECRET,
            algorithm=self.settings.JWT_ALGORITM
        )
        return token
