from core.configs import settings
from sqlalchemy import Column, Integer, String
from typing import Optional


class CursoModel(settings.DBBaseModel):
    __tablename__ = "cursos"
    
    id: Optional[int] = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    aulas: int = Column(Integer)
    horas: int = Column(Integer)
    