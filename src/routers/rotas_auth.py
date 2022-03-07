from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from src.infra.providers import hash_provider
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.schemas import schemas

router = APIRouter()


@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=schemas.UsuarioSimples)
def signup(usuario: schemas.Usuario, db: Session = Depends(get_db)):

    usuario_localizado = RepositorioUsuario(db).obter_por_telefone(usuario.telefone)
    if usuario_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Já existe um usuario com esse telefone')

    usuario.senha = hash_provider.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado
