from typing import List

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from src.routers.auth_utils import obter_usuario_logado
from src.schemas import schemas
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto

router = APIRouter()


@router.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=schemas.Produto)
def criar_produto(produto: schemas.Produto, usuario: schemas.Usuario = Depends(obter_usuario_logado),
                  db: Session = Depends(get_db)):
    produto.usuario_id = usuario.id
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@router.put('/produtos/{id_produto}', status_code=status.HTTP_201_CREATED, response_model=schemas.ProdutoSimples)
def editar_produto(id_produto: int, produto: schemas.Produto, db: Session = Depends(get_db)):
    RepositorioProduto(db).editar(id_produto, produto)
    produto.id = id_produto
    return produto


@router.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[schemas.Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos


@router.get('/produtos/{id_produto}')
def exibir_produto(id_produto: int, db: Session = Depends(get_db)):
    produto_localizado = RepositorioProduto(db).listar_por_id(id_produto)
    if not produto_localizado:
        raise HTTPException(status_code=404, detail='Produto não localizado')
    return produto_localizado


@router.delete('/produtos/{id_produto}')
def deletar_produto(id_produto: int, db: Session = Depends(get_db)):
    RepositorioProduto(db).remover(id_produto)
    return {"msg": "produto deletado"}
