"""delete amout as primary key

Revision ID: bd2ae9d7baa5
Revises: aef8b43494ae
Create Date: 2026-04-07 18:07:34.428076

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd2ae9d7baa5'
down_revision: Union[str, Sequence[str], None] = 'aef8b43494ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_constraint('amount','records',type_='primary')


def downgrade() -> None:
    """Downgrade schema."""
    op.create_primary_key('amount','records',['amount',])
