from typing import Optional, List

from pydantic.main import BaseModel


class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: str
    disponivel: bool

    class Config:
        orm_mode = True


class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    senha: str
    telefone: str
    produtos: List[ProdutoSimples] = []

    class Config:
        orm_mode = True


class UsuarioSimples(BaseModel):
    id: int
    nome: str
    telefone: str

    class Config:
        orm_mode = True


class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: Optional[int]
    usuario: Optional[UsuarioSimples]

    class Config:
        orm_mode = True


class Pedido(BaseModel):
    id: Optional[int] = None
    usuario_id: Optional[int]
    produto_id: Optional[int]
    quantidade: int
    local_entrega: str
    entrega_ou_retirada: str
    observacoes: Optional[str] = 'Sem observações'
