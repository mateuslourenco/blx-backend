from fastapi import APIRouter, status, Depends
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
