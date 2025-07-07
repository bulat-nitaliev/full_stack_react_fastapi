from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = '.env'

    DB_DRIVER:str = 'postgresql+asyncpg'
    DB_HOST:str = ''
    DB_PORT:str = ''
    DB_USER:str = ''
    DB_PASS:str = ''
    DB_NAME:str = ""
    TEST_DB_NAME:str = 'test'

    JWT_SECRET: str
    JWT_ALGORITM: str

    @property
    def get_db_url(self):
        return f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
    

settings = Settings()