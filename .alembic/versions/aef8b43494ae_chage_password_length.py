"""chage_password_length

Revision ID: aef8b43494ae
Revises: 599412335eec
Create Date: 2026-04-07 16:35:19.113839

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aef8b43494ae'
down_revision: Union[str, Sequence[str], None] = '599412335eec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('users','password',existing_type=sa.String(8),type_=sa.String(500))


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('users','password',type_=sa.String(8),existing_type=sa.String(500))
