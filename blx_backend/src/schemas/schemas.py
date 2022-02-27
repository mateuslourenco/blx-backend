from typing import Optional, List

from pydantic.main import BaseModel


class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    minhas_vendas: List[Pedido]
    meus_pedidos: List[Pedido]
    meus_produtos: List[Produto]


class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhe: str
    preco: float
    diponivel: bool = False

    class Config:
        orm_mode = True


class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'
