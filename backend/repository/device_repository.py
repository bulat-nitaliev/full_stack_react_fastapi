from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Device, DeviceInfo
from sqlalchemy import select, join, desc


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
    ) -> Device:
        async with self.db_session as session:
            db_device = Device(
                name=name, price=price, img=img, type_id=type_id, brand_id=brand_id
            )
            session.add(db_device)
            await session.commit()
            await session.refresh(db_device)

            return db_device
        
    async def get_devices(self,limit:int, offset:int):
      async with self.db_session as session:
          stmt = select(Device).order_by(desc(Device.id)).limit(limit=limit).offset(offset=offset)
          res = await session.execute(stmt)
          return res.scalars().all()
      

    async def get_devices_by_brand_type(self,brand_id:int, type_id:int,limit:int, offset:int)->list[Device]|None:
        async with self.db_session as session:
          stmt = select(Device).where(Device.brand_id==brand_id,Device.type_id==type_id,).order_by(desc(Device.id)).limit(limit=limit).offset(offset=offset)
          res = await session.execute(stmt)
          return res.scalars().all()
        

    async def get_devices_by_brand_id(self,brand_id:int,limit:int, offset:int)->list[Device]|None:
        async with self.db_session as session:
          stmt = select(Device).where(Device.brand_id==brand_id).order_by(desc(Device.id)).limit(limit=limit).offset(offset=offset)
          res = await session.execute(stmt)
          return res.scalars().all()
        

    async def get_devices_by_type_id(self,type_id:int,limit:int, offset:int)->list[Device]|None:
        async with self.db_session as session:
          stmt = select(Device).where(Device.type_id==type_id,).order_by(desc(Device.id)).limit(limit=limit).offset(offset=offset)
          res = await session.execute(stmt)
          return res.scalars().all()


    async def get_device_by_id(self,device_id:int)->Device:
        async with self.db_session as session:
            stmt = select(Device).where(Device.id==device_id)
            res = await session.execute(stmt)
            return res.scalar_one_or_none()

        #   stmt = (
        #         select(
        #             Device.id,
        #             Device.name,
        #             Device.price,
        #             DeviceInfo.title,
        #             DeviceInfo.description,
        #             Device.rating,
        #             Device.img,
        #             Device.brand_id,
        #             Device.type_id
        #         )
        #         .select_from(Device)
        #         .join(DeviceInfo, Device.id == DeviceInfo.device_id)
        #     )
        #   res = await session.execute(stmt)
        #   c = ['id','name', 'price', 'title', 'description', 'rating', 'img', 'brand_id', 'type_id']
        #   print([dict(zip(c, i)) for i in res.all()])
        #   return [dict(zip(c, i)) for i in res.all()]
