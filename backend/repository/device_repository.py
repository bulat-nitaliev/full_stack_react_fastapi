from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Device, DeviceInfo
from sqlalchemy import select, join


@dataclass
class DeviceRepository:
    db_session: AsyncSession

    async def add_device(
            self,
        name: str,
        price: float,
        type_id: int,
        brand_id: int,
        img: str,
        title: str,
        description: str,
    ) -> Device:
        async with self.db_session as session:
            db_device = Device(
                name=name, price=price, img=img, type_id=type_id, brand_id=brand_id
            )
            session.add(db_device)
            await session.commit()
            await session.refresh(db_device)

            db_info = DeviceInfo(
                title=title, description=description, device_id=db_device.id
            )
            session.add(db_info)

            await session.commit()
            await session.refresh(db_device)

            
            return db_device
        
    async def get_devices(self):
      async with self.db_session as session:
          stmt = (
                select(
                    Device.id,
                    Device.name,
                    Device.price,
                    DeviceInfo.title,
                    DeviceInfo.description,
                    Device.rating,
                    Device.img,
                    Device.brand_id,
                    Device.type_id
                )
                .select_from(Device)
                .join(DeviceInfo, Device.id == DeviceInfo.device_id)
            )
          res = await session.execute(stmt)
          c = ['id','name', 'price', 'title', 'description', 'rating', 'img', 'brand_id', 'type_id']
          print([dict(zip(c, i)) for i in res.all()])
          return [dict(zip(c, i)) for i in res.all()]
