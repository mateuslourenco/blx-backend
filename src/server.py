from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto

criar_db()

app = FastAPI()


@app.get('/')
def home():
    return {'msg': 'BLX - Back-end API'}

# PRODUTOS


@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=schemas.Produto)
def criar_produto(produto: schemas.Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[schemas.Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos


# USUARIOS


@app.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=schemas.Usuario)
def criar_usuario(usuario: schemas.Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado


@app.get('/usuarios', status_code=status.HTTP_200_OK, response_model=List[schemas.Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios
