from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from dependency import get_request_user_id, get_rating_service
from exception.store import DeviceNotFoundException
from schemas.rating import RatingSchema
from service.rate_service import RateService


router = APIRouter(prefix='/rating', tags=['rating'])


@router.post('/', response_model=RatingSchema)
async def add_rating_by_device(
  user_id: Annotated[int, Depends(get_request_user_id)],
  body: RatingSchema,
  rate_service: Annotated[RateService, Depends(get_rating_service)]
):
  try:
    return await rate_service.add_rate(
      rate=body.rate, 
      device_id=body.device_id, 
      user_id=user_id
      )
  except DeviceNotFoundException as e:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=e.detail
    )