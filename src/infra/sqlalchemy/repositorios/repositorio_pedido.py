from sqlalchemy import select
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
                                  local_de_entrega=pedido.local_de_entrega,
                                  entrega_ou_retirada=pedido.entrega_ou_retirada,
                                  observacoes=pedido.observacoes
                                  )
        self.session.add(db_pedido)
        self.session.commit()
        self.session.refresh(db_pedido)
        return db_pedido

    def exibir(self, id_pedido: int):
        consulta = select(models.Pedido).where(models.Pedido.id == id_pedido)
        produto = self.session.execute(consulta).scalars().first()
        return produto

    def listar_pedidos_usuario(self, id_usuario: int) -> models.Pedido:
        consulta = select(models.Pedido).where(models.Pedido.usuario_id == id_usuario)
        pedidos = self.session.execute(consulta).scalars().all()
        return pedidos

    def listar_vendas_por_usuario(self, id_usuario: int):
        consulta = select(models.Pedido).join_from(models.Pedido, models.Produto).where(
            models.Produto.usuario_id == id_usuario)
        vendas = self.session.execute(consulta).scalars().all()
        return vendas
