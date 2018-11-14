"""empty message

Revision ID: 8f397bb929d8
Revises: 3b36ecb33e27
Create Date: 2018-11-08 10:42:22.342272

"""

# revision identifiers, used by Alembic.
revision = '8f397bb929d8'
down_revision = '3b36ecb33e27'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('member_since', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'member_since')
    op.drop_column('users', 'last_seen')
    # ### end Alembic commands ###