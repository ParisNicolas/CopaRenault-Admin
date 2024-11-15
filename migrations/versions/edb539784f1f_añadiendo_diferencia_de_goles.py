"""Añadiendo diferencia de goles

Revision ID: edb539784f1f
Revises: 819f7e24f82b
Create Date: 2024-11-15 11:14:33.463273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edb539784f1f'
down_revision = '819f7e24f82b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('equipos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('diferncia_gol', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('equipos', schema=None) as batch_op:
        batch_op.drop_column('diferncia_gol')

    # ### end Alembic commands ###
