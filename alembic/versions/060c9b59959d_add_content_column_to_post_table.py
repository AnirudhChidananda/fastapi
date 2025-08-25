"""add content column to post table

Revision ID: 060c9b59959d
Revises: c16824fd86e3
Create Date: 2025-08-25 13:53:39.850081

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '060c9b59959d'
down_revision: Union[str, Sequence[str], None] = 'c16824fd86e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', "content")
    pass
