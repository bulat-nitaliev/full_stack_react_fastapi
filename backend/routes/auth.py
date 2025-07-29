from fastapi import APIRouter, Depends, HTTPException, status
from schemas.auth_schema import LoginSchema, Login
from service.auth_service import AuthService
from dependency import get_auth_service, get_request_user_id
from exception.user import UserNotCorrectPasswordException, UserNotFoundException
from typing import Annotated



router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=LoginSchema)
async def login(
    body: Login, auth_service: AuthService = Depends(get_auth_service)
) -> LoginSchema:
    try:
        print(body)
        return await auth_service.login(email=body.email, password=body.password)
    except UserNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)
    except UserNotCorrectPasswordException as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=e.detail)



@router.get('/')
async def check(
    user_id: Annotated[int, Depends(get_request_user_id)],
    auth_service: Annotated[AuthService, Depends(get_auth_service)]
    ):
    print(user_id)
    return await auth_service.check(user_id=user_id)