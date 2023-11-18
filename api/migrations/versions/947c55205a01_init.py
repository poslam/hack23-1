"""init

Revision ID: 947c55205a01
Revises: 
Create Date: 2023-11-18 12:32:43.075310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '947c55205a01'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.TEXT(), nullable=True),
    sa.Column('second_name', sa.TEXT(), nullable=True),
    sa.Column('third_name', sa.TEXT(), nullable=True),
    sa.Column('email', sa.TEXT(), nullable=True),
    sa.Column('password', sa.TEXT(), nullable=True),
    sa.Column('type', sa.Enum('admin', 'driver', 'packer', name='usertypes'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('client')
    # ### end Alembic commands ###