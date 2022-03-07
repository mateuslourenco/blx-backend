from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from src.infra.providers import hash_provider, token_provider
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.routers.auth_utils import obter_usuario_logado
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


@router.post('/signin', response_model=schemas.LoginSucesso)
def signin(login_data: schemas.LoginData, db: Session = Depends(get_db)):
    senha = login_data.senha
    telefone = login_data.telefone

    usuario = RepositorioUsuario(db).obter_por_telefone(telefone)

    # Validar se usuario existe e se senha está correta
    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Telefone ou senha incorretos')

    senha_valida = hash_provider.verificar_hash(senha, usuario.senha)

    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Telefone ou senha incorretos')

    # JWT
    token = token_provider.criar_access_token({'sub': usuario.telefone})
    return schemas.LoginSucesso(usuario=usuario, token=token)


@router.get('/me', response_model=schemas.UsuarioSimples)
def me(usuario: schemas.Usuario = Depends(obter_usuario_logado)):
    return usuario
