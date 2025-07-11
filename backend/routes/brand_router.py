from exception.store import TypeExistsException
from fastapi import APIRouter, Depends, HTTPException, status
from dependency import get_brand_service
from service.brand_service import BrandService
from schemas.type_schema import CreateTypeBrandSchema, TypeBrandSchema

router = APIRouter(prefix="/brand", tags=["brand"])


@router.post("/", response_model=TypeBrandSchema)
async def create_brand(
    body: CreateTypeBrandSchema,
    brand_service: BrandService = Depends(get_brand_service),
):
    try:
        return await brand_service.create_brand(body=body)
    except TypeExistsException as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=e.detail)


@router.get("/", response_model=list[TypeBrandSchema])
async def get_brands(
    brand_service: BrandService = Depends(get_brand_service),
) -> TypeBrandSchema:
    return await brand_service.get_brands()


@router.get("/{brand_id}", response_model=TypeBrandSchema)
async def get_brand_by_id(
    brand_id: int, brand_service: BrandService = Depends(get_brand_service)
) -> TypeBrandSchema:
    return await brand_service.get_brand_by_id(id=brand_id)
