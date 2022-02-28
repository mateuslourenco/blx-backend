from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette import status

from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.schemas.schemas import Produto
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto

criar_db()

app = FastAPI()


@app.get('/')
def home():
    return {'msg': 'BLX - Back-end API'}


@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=Produto)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos
