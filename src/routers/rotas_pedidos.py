from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido
from src.schemas import schemas

router = APIRouter()


@router.post('/pedidos', status_code=status.HTTP_201_CREATED)
def fazer_pedido(pedido: schemas.Pedido, db: Session = Depends(get_db)):
    pedido_criado = RepositorioPedido(db).criar(pedido)
    pedido_criado.usuario_id = pedido.usuario_id
    pedido_criado.produto_id = pedido.produto_id
    return pedido_criado


@router.get('/pedidos/{id_pedido}')
def exibir_pedido(id_pedido: int, db: Session = Depends(get_db)):
    pedido_localizado = RepositorioPedido(db).exibir(id_pedido)
    if not pedido_localizado:
        raise HTTPException(status_code=404, detail='Pedido não localizado')
    return pedido_localizado


@router.get('/{id_usuario}/pedidos')
def listar_pedidos_por_usuario(id_usuario: int, db: Session = Depends(get_db)):
    pedidos_localizados = RepositorioPedido(db).listar_pedidos_usuario(id_usuario)
    if not pedidos_localizados:
        raise HTTPException(status_code=404, detail='Usuario sem pedidos realizados')
    return pedidos_localizados
