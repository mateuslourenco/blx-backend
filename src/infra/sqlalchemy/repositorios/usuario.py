from sqlalchemy import select
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.models import models
from src.schemas import schemas


class RepositorioUsuario:

    def __init__(self, session: Session):
        self.session = session

    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(nome=usuario.nome,
                                    senha=usuario.senha,
                                    telefone=usuario.telefone,
                                    )
        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)
        return db_usuario

    def listar(self):
        stmt = select(models.Usuario)
        usuarios = self.session.execute(stmt).scalars().all()
        return usuarios

    def obter(self):
        pass

    def remover(self):
        pass
