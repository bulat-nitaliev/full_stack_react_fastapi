from fastapi import APIRouter, Depends, HTTPException, status
from schemas.user_schema import UserCreate, UserSchema
from service.user_service import UserService
from dependency import get_user_service
from exception.user import UserExistsException


router = APIRouter(prefix="/user", tags=["user"])


@router.post("/", response_model=UserSchema)
async def create_user(
    body: UserCreate, user_service: UserService = Depends(get_user_service)
) -> UserSchema:
    try:
        return await user_service.create_user(body=body)
    except UserExistsException as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=e.detail)


@router.get("/", response_model=list[UserSchema])
async def get_users(
    user_service: UserService = Depends(get_user_service),
) -> UserSchema:
    return await user_service.get_users()
