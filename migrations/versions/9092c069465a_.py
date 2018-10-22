"""empty message

Revision ID: 9092c069465a
Revises: 5ee9905def1a
Create Date: 2018-10-21 19:07:26.019494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9092c069465a'
down_revision = '5ee9905def1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stats', sa.Column('date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stats', 'date')
    # ### end Alembic commands ###