from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from dependency import get_request_user_id, get_basket_service
from schemas.basket_device_schema import BasketDeviceSchema
from exception.store import DeviceNotFoundException
from service.basket_service import BasketService

router = APIRouter(
  prefix='/basket_device',
  tags=['basket_device']
  )


@router.post('/')
async def add_device(
  user_id: Annotated[int, Depends(get_request_user_id)],
  body: BasketDeviceSchema,
  basket_service: Annotated[BasketService, Depends(get_basket_service)]
):
  try:
    return await basket_service.add_device(
      device_id=body.device_id, 
      user_id=user_id
      )
  except DeviceNotFoundException as e:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=e.detail
    )
  

@router.get('/', response_model=list[BasketDeviceSchema])
async def get_device(
  user_id: Annotated[int, Depends(get_request_user_id)],
  basket_service: Annotated[BasketService, Depends(get_basket_service)]
):
  try:
    return await basket_service.get_device(
      user_id=user_id
      )
  except DeviceNotFoundException as e:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=e.detail
    )
  






# post добавление в корзину

# get посмотреть корзину


# delete удаление из корзины