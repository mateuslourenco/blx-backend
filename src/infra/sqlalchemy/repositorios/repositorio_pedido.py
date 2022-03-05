from sqlalchemy.orm import Session

from src.infra.sqlalchemy.models import models
from src.schemas import schemas


class RepositorioPedido:
    def __init__(self, db: Session):
        self.session = db

    def criar(self, pedido: schemas.Pedido):
        db_pedido = models.Pedido(usuario_id=pedido.usuario_id,
                                  produto_id=pedido.produto_id,
                                  quantidade=pedido.quantidade,
                                  local_de_entrega=pedido.local_entrega,
                                  entrega_ou_retirada=pedido.entrega_ou_retirada,
                                  observacoes=pedido.observacoes
                                  )
        self.session.add(db_pedido)
        self.session.commit()
        self.session.refresh(db_pedido)
        return db_pedido
