"""add forign key and owner_id column  to post table

Revision ID: 8e3c47b6c8d0
Revises: c6ce81318c2e
Create Date: 2025-08-25 14:41:07.223534

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e3c47b6c8d0'
down_revision: Union[str, Sequence[str], None] = 'c6ce81318c2e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table='posts', referent_table='users',local_cols=['owner_id'], 
    remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
