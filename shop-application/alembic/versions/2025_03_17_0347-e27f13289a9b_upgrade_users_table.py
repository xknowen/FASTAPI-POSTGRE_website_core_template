"""upgrade users table

Revision ID: e27f13289a9b
Revises: 3d39b0e94f2f
Create Date: 2025-03-17 03:47:30.109937

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e27f13289a9b'
down_revision: Union[str, None] = '3d39b0e94f2f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('foo', sa.Integer(), nullable=False))
    op.add_column('users', sa.Column('bar', sa.Integer(), nullable=False))
    op.create_unique_constraint(op.f('uqusers_foo_bar'), 'users', ['foo', 'bar'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(op.f('uqusers_foo_bar'), 'users', type_='unique')
    op.drop_column('users', 'bar')
    op.drop_column('users', 'foo')
