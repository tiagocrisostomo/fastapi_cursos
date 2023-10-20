from core.configs import settings
from sqlalchemy import Column, Integer, String 


class UsuarioModel(settings.DBBaseModel):
    __tablename__ = "usuarios"
    
        
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(120))
    email: str = Column(String(120))
    senha: str = Column(String(8))
    