from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
from starlette import status

from src.infra.providers import token_provider
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


def obter_usuario_logado(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    expt = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido')

    try:
        telefone = token_provider.verificar_access_token(token)
    except JWTError:
        raise expt

    if not telefone:
        raise expt

    usuario = RepositorioUsuario(db).obter_por_telefone(telefone)

    if not usuario:
        raise expt

    return usuario
