"""empty message

Revision ID: 3af28fcaacf0
Revises: 62b0f04229d5
Create Date: 2023-11-12 22:52:22.862769

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3af28fcaacf0'
down_revision: Union[str, None] = '62b0f04229d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
