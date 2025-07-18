from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status, Form
from db.models import Device, DeviceInfo
from dependency import get_device_service
from service.device_service import DeviceService
from schemas.device_schema import DeviceSchema, OneDeviceSchema
from exception.store import DeviceNotFoundException


router = APIRouter(prefix="/device", tags=["device"])


@router.post("/", response_model=DeviceSchema)
async def create_device(
    name: str = Form(),
    price: float = Form(),
    type_id: int = Form(),
    brand_id: int = Form(),
    # title: str = Form(),
    # description: str = Form(),
    image: UploadFile = File(None),
    devise_service: DeviceService = Depends(get_device_service),
) -> DeviceSchema:
    image_path = await devise_service.get_path_img(image=image)
    return await devise_service.create_device(
        name=name,
        price=price,
        type_id=type_id,
        brand_id=brand_id,
        img=image_path,
        # title=title,
        # description=description,
    )


@router.get("", response_model=list[DeviceSchema])
async def get_all(
    devise_service: DeviceService = Depends(get_device_service),
    brand_id: int = None,
    type_id: int = None,
    limit: int = 9,
    page: int = 1,
) -> list:
    offset = limit * page - limit
    res = await devise_service.get_all(
        brand_id=brand_id, type_id=type_id, limit=limit, offset=offset
    )
    print(res)
    return res


@router.get("/{device_id}", response_model=OneDeviceSchema)
async def get_device_by_id(
    device_id: int, device_service: DeviceService = Depends(get_device_service)
) -> OneDeviceSchema:
    try:
        return await device_service.get_device_by_id(device_id=device_id)
    except DeviceNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)
