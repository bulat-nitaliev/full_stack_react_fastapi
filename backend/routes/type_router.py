from exception.store import TypeExistsException
from fastapi import APIRouter, Depends, HTTPException, status
from dependency import get_type_service
from service.type_service import TypeService
from schemas.type_schema import CreateTypeBrandSchema, TypeBrandSchema

router = APIRouter(prefix="/type", tags=["type"])


@router.post("/", response_model=TypeBrandSchema)
async def create_type(
    body: CreateTypeBrandSchema, type_service: TypeService = Depends(get_type_service)
):
    try:
        return await type_service.create_type(body=body)
    except TypeExistsException as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=e.detail)


@router.get("/", response_model=list[TypeBrandSchema])
async def get_types(
    type_service: TypeService = Depends(get_type_service),
) -> TypeBrandSchema:
    return await type_service.get_types()
