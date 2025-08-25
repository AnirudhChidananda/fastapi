"""creaate posts table

Revision ID: c16824fd86e3
Revises: 
Create Date: 2025-08-25 08:50:38.133612

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c16824fd86e3'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('tittle',sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
