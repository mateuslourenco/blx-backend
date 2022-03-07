from typing import List

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto
from src.routers.auth_utils import obter_usuario_logado
from src.schemas import schemas

router = APIRouter()


@router.post('/pedidos', status_code=status.HTTP_201_CREATED, response_model=schemas.Pedido)
def fazer_pedido(pedido: schemas.Pedido, usuario: schemas.Usuario = Depends(obter_usuario_logado),
                 db: Session = Depends(get_db)):
    produto_localizado = RepositorioProduto(db).listar_por_id(pedido.produto_id)

    if not produto_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Produto não localizado')

    pedido.usuario_id = usuario.id
    pedido_criado = RepositorioPedido(db).criar(pedido)
    pedido_criado.usuario_id = pedido.usuario_id
    pedido_criado.produto_id = pedido.produto_id
    return pedido_criado


@router.get('/pedidos/{id_pedido}', response_model=schemas.Pedido)
def exibir_pedido(id_pedido: int, usuario: schemas.Usuario = Depends(obter_usuario_logado),
                  db: Session = Depends(get_db)):

    pedido_localizado = RepositorioPedido(db).exibir(id_pedido)
    if not pedido_localizado:
        raise HTTPException(status_code=404, detail='Pedido não localizado')
    return pedido_localizado


@router.get('/pedidos', response_model=List[schemas.Pedido])
def listar_pedidos_por_usuario(usuario: schemas.Usuario = Depends(obter_usuario_logado), db: Session = Depends(get_db)):
    pedidos_localizados = RepositorioPedido(db).listar_pedidos_usuario(usuario.id)
    if not pedidos_localizados:
        raise HTTPException(status_code=404, detail='Usuario sem pedidos realizados')
    return pedidos_localizados


@router.get('/pedidos/{id_usuario}/vendas', response_model=List[schemas.Pedido])
def listar_vendas_por_usuario(id_usuario: int, db: Session = Depends(get_db)):
    vendas_localizadas = RepositorioPedido(db).listar_vendas_por_usuario(id_usuario)
    if not vendas_localizadas:
        raise HTTPException(status_code=404, detail='Usuario sem vendas realizadas')
    return vendas_localizadas
