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
    produtos: List[ProdutoSimples] = []

    class Config:
        orm_mode = True


class UsuarioSemProdutos(BaseModel):
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
    usuario: Optional[UsuarioSemProdutos]

    class Config:
        orm_mode = True


class LoginData(BaseModel):
    telefone: str
    senha: str


class LoginSucesso(BaseModel):
    usuario: UsuarioSimples
    token: str


class Pedido(BaseModel):
    id: Optional[int] = None
    usuario_id: Optional[int]
    produto_id: Optional[int]
    quantidade: int
    local_de_entrega: str
    entrega_ou_retirada: str
    observacoes: Optional[str] = 'Sem observações'

    usuario: Optional[UsuarioSimples]
    produto: Optional[ProdutoSimples]

    class Config:
        orm_mode = True
