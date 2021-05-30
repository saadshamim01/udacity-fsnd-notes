"""empty message

Revision ID: 77d74915ca47
Revises: 9f0cbbeca511
Create Date: 2021-03-16 01:22:56.642785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77d74915ca47'
down_revision = '9f0cbbeca511'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###