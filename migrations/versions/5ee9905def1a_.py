"""empty message

Revision ID: 5ee9905def1a
Revises: 790cad397c1b
Create Date: 2018-10-21 18:33:59.192317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ee9905def1a'
down_revision = '790cad397c1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stats',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ip_dpid', sa.String(length=50), nullable=True),
    sa.Column('rx', sa.Integer(), nullable=True),
    sa.Column('tx', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stats')
    # ### end Alembic commands ###