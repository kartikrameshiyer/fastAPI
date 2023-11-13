"""empty message

Revision ID: 62b0f04229d5
Revises: 3220334ec71b
Create Date: 2023-11-12 22:06:30.042524

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '62b0f04229d5'
down_revision: Union[str, None] = '3220334ec71b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
