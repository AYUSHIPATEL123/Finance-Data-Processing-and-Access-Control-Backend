"""add new in forign key att in record

Revision ID: bb9230f5d526
Revises: 6e93b88b8709
Create Date: 2026-05-25 18:31:00.694593

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb9230f5d526'
down_revision: Union[str, Sequence[str], None] = '6e93b88b8709'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    

    pass



def downgrade() -> None:
    op.drop_constraint(
        "fk_records_user_id",
        "records",
        type_="foreignkey"
    )

    # Restore old FK
    op.create_foreign_key(
        "records_ibfk_1",
        "records",
        "users",
        ["user_id"],
        ["id"]
    )
