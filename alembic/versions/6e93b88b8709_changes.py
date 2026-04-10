"""changes

Revision ID: 6e93b88b8709
Revises: 
Create Date: 2026-04-09 18:19:23.891221

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e93b88b8709'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_constraint('password','users',type_='unique')
    op.alter_column('users','password',existing_type=sa.String(8),type_=sa.String(500))
    op.drop_constraint('amount','records',type_='primary')


def downgrade() -> None:
    """Downgrade schema."""
    op.create_unique_constraint('password','users',['password'])
    op.alter_column('users','password',type_=sa.String(8),existing_type=sa.String(500))
    op.create_primary_key('amount','records',['amount',]) 

