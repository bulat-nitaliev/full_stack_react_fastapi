from repository.user_repository import UserRepository
from dataclasses import dataclass
from schemas.auth_schema import LoginSchema
from db.models import User 
from exception.user import UserNotCorrectPasswordException, UserNotFoundException
from settings.config import Settings
from jose import jwt, JWTError
from datetime import datetime, timedelta, UTC
from security import secret


@dataclass
class AuthService:
    user_repo: UserRepository
    settings: Settings

    async def login(self, email: str, password: str) -> LoginSchema:
        user = await self.user_repo.get_user_by_email(email=email)
        self.validate(user=user, password=password)
        access_token = self.create_access_token(user_id=user.id, email=user.email, role=user.role)

        return LoginSchema(user_id=user.id, access_token=access_token)

    
    def validate(self,user: User, password: str):
        if not user:
            raise UserNotFoundException
        
        if not secret.verify_password(
            plain_password=password, 
            hashed_password=user.password
            ):
            raise UserNotCorrectPasswordException

    def create_access_token(self, user_id: int, email:str, role:str):
        dt_expire = (datetime.now(tz=UTC) + timedelta(days=7)).timestamp()
        token = jwt.encode(
            {
                "user_id": user_id, 
                "email":email,
                "role":role,  
                "exp": dt_expire
                },
            key=self.settings.JWT_SECRET,
            algorithm=self.settings.JWT_ALGORITM,
        )
        return token
