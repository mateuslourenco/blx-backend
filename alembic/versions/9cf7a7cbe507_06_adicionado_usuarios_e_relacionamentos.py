"""06_Adicionado_usuarios_e_relacionamentos

Revision ID: 9cf7a7cbe507
Revises: 5e1814b6e1ba
Create Date: 2022-02-28 21:10:36.957485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cf7a7cbe507'
down_revision = '5e1814b6e1ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('produto', sa.Column('usuario_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'produto', 'usuario', ['usuario_id'], ['id'])
    op.add_column('usuario', sa.Column('senha', sa.String(), nullable=True))
    op.add_column('usuario', sa.Column('telefone', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'telefone')
    op.drop_column('usuario', 'senha')
    op.drop_constraint(None, 'produto', type_='foreignkey')
    op.drop_column('produto', 'usuario_id')
    # ### end Alembic commands ###
