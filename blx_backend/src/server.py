from fastapi import FastAPI
from blx_backend.src.schemas.schemas import Produto
from blx_backend.src.infra.sqlalchemy.repositorios.produto import RepositorioProduto

app = FastAPI()


@app.post('/produtos')
def criar_produto(produto: Produto):
    produto_criado = RepositorioProduto().criar(produto)
    return produto_criado


@app.get('/produtos')
def listar_produtos():
    return {'msg': 'Listagem de produtos'}
