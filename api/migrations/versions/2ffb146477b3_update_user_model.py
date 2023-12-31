"""update user model

Revision ID: 2ffb146477b3
Revises: 947c55205a01
Create Date: 2023-11-18 22:54:26.082552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ffb146477b3'
down_revision = '947c55205a01'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client', sa.Column('car_num', sa.TEXT(), nullable=True))
    op.add_column('client', sa.Column('active_shift', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('client', 'active_shift')
    op.drop_column('client', 'car_num')
    # ### end Alembic commands ###
