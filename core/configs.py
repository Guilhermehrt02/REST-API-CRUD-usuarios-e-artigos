from typing import List
from typing_extensions import Type

from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://guilherme:Guilherme02@localhost:5432/faculdade'
    DBBaseModel: Type[Base] = Base  

    #segredo da api para gerar um hash
    JWT_SECRET: str = 'B0-pBgbmrwpMP5B0A-uww8ropNlbi4GlxKpSsdfNOgM'
    """
    import secrets

    token: str = secrets.token_urlsafe(32)
    """

    ALGORITHM: str = 'HS256'
    #60 min * 24 hrs * 7 dias => 1 semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True

settings: Settings = Settings()
