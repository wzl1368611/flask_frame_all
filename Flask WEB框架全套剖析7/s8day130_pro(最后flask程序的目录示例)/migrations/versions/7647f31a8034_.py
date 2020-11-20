"""empty message

Revision ID: 7647f31a8034
Revises: dfd8eb5cf61c
Create Date: 2018-05-04 14:23:42.784938

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7647f31a8034'
down_revision = 'dfd8eb5cf61c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('name', table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=32), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('name', 'users', ['name'], unique=True)
    # ### end Alembic commands ###
