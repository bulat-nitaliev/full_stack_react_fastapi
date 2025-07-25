from dataclasses import dataclass
from repository.user_repository import UserRepository
from schemas.user_schema import UserSchema
from exception.user import UserExistsException
from security import secret


@dataclass
class UserService:
    user_repo: UserRepository

    async def create_user(self, body) -> UserSchema:
        user = await self.user_repo.get_user_by_email(email=body.email)
        if user:
            raise UserExistsException
        hashed_password = secret.get_password_hash(password=body.password)
        body.password = hashed_password

        return await self.user_repo.add_user(body=body)

    async def get_users(self):
        return await self.user_repo.get_users()
