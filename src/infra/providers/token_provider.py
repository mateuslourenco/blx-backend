# CONFIG
from datetime import datetime, timedelta

from decouple import config
from jose import jwt

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = 'HS256'
EXPIRES_IN = 3000


def criar_access_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN)

    dados.update({'exp': expiracao})

    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt


def verificar_access_token(token: str):
    carga = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return carga.get('sub')
