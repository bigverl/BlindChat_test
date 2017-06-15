"""empty message

Revision ID: ab134711410a
Revises: 
Create Date: 2017-06-15 23:06:32.718000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab134711410a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('active_chats_user', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=64))
    op.alter_column('user', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=64))
    op.alter_column('waiting_list_user', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=64))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('waiting_list_user', 'id',
               existing_type=sa.String(length=64),
               type_=sa.INTEGER())
    op.alter_column('user', 'id',
               existing_type=sa.String(length=64),
               type_=sa.INTEGER())
    op.alter_column('active_chats_user', 'id',
               existing_type=sa.String(length=64),
               type_=sa.INTEGER())
    # ### end Alembic commands ###