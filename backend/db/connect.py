from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from settings.config import settings


class DataBaseHelper:
    def __init__(self, db_url: str):
        self.engine = create_async_engine(url=db_url)
        self.session_factory = async_sessionmaker(
            bind=self.engine
        )

    async def get_db_session(self):
        async with self.session_factory() as session:
            yield session
            session.aclose()


helper = DataBaseHelper(db_url=settings.get_db_url)
