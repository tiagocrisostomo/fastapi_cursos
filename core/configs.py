from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from fastapi.templating import Jinja2Templates
from pathlib import Path
from sqlalchemy.orm.decl_api import DeclarativeMeta

from typing import ClassVar


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:150883@localhost:2345/faculdade"
    DBBaseModel: ClassVar[DeclarativeMeta] = declarative_base()
    TEMPLATES: ClassVar[Jinja2Templates] = Jinja2Templates(directory='templates')
    MEDIA: ClassVar[Path] = Path('media')

    class Config:
        case_sensitive = True


settings = Settings()