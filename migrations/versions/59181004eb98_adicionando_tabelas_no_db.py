"""Adicionando tabelas no db

Revision ID: 59181004eb98
Revises: 
Create Date: 2024-10-24 23:54:53.504031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59181004eb98'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pizzas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sabor', sa.String(length=100), nullable=True),
    sa.Column('imagem', sa.String(length=100), nullable=True),
    sa.Column('ingredientes', sa.String(length=100), nullable=True),
    sa.Column('preco', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('senha', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pedidos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('pizza_id', sa.Integer(), nullable=False),
    sa.Column('data', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['pizza_id'], ['pizzas.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pedidos')
    op.drop_table('usuarios')
    op.drop_table('pizzas')
    # ### end Alembic commands ###
