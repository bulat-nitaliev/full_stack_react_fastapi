from dataclasses import dataclass
from fastapi import UploadFile
import os
import uuid
from settings.config import settings
from schemas.device_schema import DeviceSchema,ListDeviceSchema
from repository.device_repository import DeviceRepository


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
        title: str,
        description: str,
    ) -> DeviceSchema:
        return await self.device_repo.add_device(
            name=name,
            price=price,
            img=img,
            type_id=type_id,
            brand_id=brand_id,
            title=title,
            description=description,
        )
    

    async def get_all(self):
        res =  await self.device_repo.get_devices()
        res = [ListDeviceSchema(**i) for i in res]
        print(res)
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
