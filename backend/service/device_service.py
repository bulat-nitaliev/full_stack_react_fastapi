from dataclasses import dataclass
from fastapi import UploadFile
import os
import uuid
from settings.config import settings
from schemas.device_schema import DeviceSchema, OneDeviceSchema
from repository.device_repository import DeviceRepository
from exception.store import DeviceNotFoundException


@dataclass
class DeviceService:
    device_repo: DeviceRepository

    async def create_device(
        self,
        name: str,
        price: float,
        type_id: int,
        brand_id: int,
        img: str,
        # title: str,
        # description: str,
    ) -> DeviceSchema:
        return await self.device_repo.add_device(
            name=name,
            price=price,
            img=img,
            type_id=type_id,
            brand_id=brand_id,
        )

    async def get_all(self, brand_id: int, type_id: int, limit: int, offset: int):
        res = await self.get_query(
            brand_id=brand_id, type_id=type_id, limit=limit, offset=offset
        )

        return res

    async def get_path_img(self, image: UploadFile) -> str:
        os.makedirs(settings.IMAGES_DIR, exist_ok=True)
        image_path = None
        if image and image.filename:
            # Генерируем уникальное имя файла
            file_ext = os.path.splitext(image.filename)[1]
            file_name = f"{uuid.uuid4()}{file_ext}"
            image_path = os.path.join(settings.IMAGES_DIR, file_name)

            # Сохраняем файл
            with open(image_path, "wb") as buffer:
                content = await image.read()
                buffer.write(content)

            # Для доступа через URL
            image_path = f"/{settings.IMAGES_DIR}/{file_name}"

        return image_path

    async def get_device_by_id(self, device_id: int) -> OneDeviceSchema:

        if res := await self.device_repo.get_device_by_id(device_id=device_id):
            print(res.info)
            return res
        raise DeviceNotFoundException

    async def get_query(
        self, brand_id: int, type_id: int, limit: int, offset: int
    ) -> list[DeviceSchema]:
        if brand_id and type_id:
            return await self.device_repo.get_devices_by_brand_type(
                brand_id=brand_id, type_id=type_id, limit=limit, offset=offset
            )
        elif brand_id and type_id is None:
            return await self.device_repo.get_devices_by_brand_id(
                brand_id=brand_id, limit=limit, offset=offset
            )
        elif brand_id is None and type_id:
            return await self.device_repo.get_devices_by_type_id(
                type_id=type_id, limit=limit, offset=offset
            )

        return await self.device_repo.get_devices(limit=limit, offset=offset)
