from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.usuario_model import UsuarioModel
from schemas.usuario_schema import UsuarioSchema
from core.deps import get_session


router = APIRouter()


# POST Usuário
@router.post('/', status_code=status.HTTP_201_CREATED, 
        response_model=UsuarioSchema,
        description='Envia um novo usuário para cadastrar.', 
        summary="Cria um novo usuário.", 
        response_description="Usuário criado com sucesso." )
async def post_usuario(usuario: UsuarioSchema, db: AsyncSession = Depends(get_session)):
    novo_usuario = UsuarioModel(nome=usuario.nome, email=usuario.email, senha=usuario.senha)    
    db.add(novo_usuario)
    await db.commit()
    
    return novo_usuario



# GET Usuário
@router.get('/', response_model=List[UsuarioSchema],
        description='Retorna todos os usuários ou uma lista vazia.', 
        summary="Retorna todos os usuários.", 
        response_description="Usuários encontrados com sucesso.")
async def get_usuarios(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel)
        result = await session.execute(query)
        usuarios: List[UsuarioModel] = result.scalars().all()
        
        return usuarios 
    
    
    
# GET Usuário
@router.get('/{usuario_id}', response_model=UsuarioSchema, 
        status_code=status.HTTP_200_OK,
        description='Retorna o usuário informado ou detalhamento de não encontrado.', 
        summary='Retorna o usuário informado.', 
        response_description="Usuário encontrado com sucesso.")
async def get_cursos(usuario_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario = result.scalar_one_or_none()
        
        if usuario:
            return usuario
        else:
            raise HTTPException(detail="Usuário não encontrado.", status_code=status.HTTP_404_NOT_FOUND)
        
        
        
# PUT Usuário
@router.put('/{usuario_id}', response_model=UsuarioSchema, 
        status_code=status.HTTP_202_ACCEPTED,
        description='Retorna os dados do usuário informado para alteração ou curso não encontrado.', 
        summary='Altera o usuário informado.', 
        response_description="Usuário alterado com sucesso." )
async def put_curso(usuario_id: int, usuario: UsuarioSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario_up = result.scalar_one_or_none()
        
        if usuario_up:
            usuario_up.nome = usuario.nome
            usuario_up.email =  usuario.email
            usuario_up.senha =  usuario.senha
            
            await session.commit()
            
            return usuario_up
        else:
            raise HTTPException(detail="Usuário não encontrado.", status_code=status.HTTP_404_NOT_FOUND)
        
    
        
# DELETE Usuário
@router.delete('/{usuario_id}', status_code=status.HTTP_204_NO_CONTENT,
        description='Envia um usuário para ser deletado.', 
        summary="Deleta o usuário informado.",          
        response_description="Usuário deletado com sucesso.")
async def delete_curso(usuario_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuario_id)
        result = await session.execute(query)
        usuario_del = result.scalar_one_or_none()
        
        if usuario_del:
            await session.delete(usuario_del)
            await session.commit()
                        
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Usuário não encontrado.", status_code=status.HTTP_404_NOT_FOUND)
        