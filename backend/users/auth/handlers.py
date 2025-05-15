from fastapi import APIRouter, Depends, HTTPException, status
from .schema import LoginSchema, Login
from users.auth.service import AuthService
from dependency import get_auth_service
from exception.user import UserNotCorrectPasswordException, UserNotFoundException




router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.post('/login',response_model=LoginSchema)
async def login(
    body:Login,
    auth_service:AuthService=Depends(get_auth_service)
    )->LoginSchema:
    try:
        print(body)
        return await auth_service.login(
            email=body.email,
            password=body.password
            )
    except UserNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.detail
        )
    except UserNotCorrectPasswordException as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e.detail
        )