from typing import List

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.schemas import schemas

router = APIRouter()


@router.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=schemas.Usuario)
def criar_usuario(usuario: schemas.Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado


@router.get('/usuarios', status_code=status.HTTP_200_OK, response_model=List[schemas.Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios
