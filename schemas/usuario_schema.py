from typing import Optional
from pydantic import BaseModel as SCBaseModel


class UsuarioSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    email: str
    senha: str
    
    class Config:
        from_attributes = True
        