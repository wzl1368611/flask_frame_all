"""empty message

Revision ID: 19d7c4a40749
Revises: 7647f31a8034
Create Date: 2018-05-04 14:24:15.099787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19d7c4a40749'
down_revision = '7647f31a8034'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('pwd', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
