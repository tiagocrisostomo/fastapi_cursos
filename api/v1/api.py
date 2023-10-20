from fastapi import APIRouter
from api.v1.endpoints import curso, usuario


api_router = APIRouter()
api_router.include_router(curso.router, prefix='/cursos', tags=["cursos"])
api_router.include_router(usuario.router, prefix='/usuarios', tags=["usuarios"])

#/api/v1/cursos