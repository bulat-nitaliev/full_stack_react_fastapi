from dataclasses import dataclass
from .repository import UserRepository
from .schema import UserSchema
from exception.user import UserExistsException


@dataclass
class UserService:
    user_repo:UserRepository

    async def create_user(self, body)->UserSchema:
        user = await self.user_repo.get_user_by_email(email=body.email)
        if user:
            raise UserExistsException
        
        return await self.user_repo.add_user(body=body)
    
    async def get_users(self):
        return await self.user_repo.get_users()


