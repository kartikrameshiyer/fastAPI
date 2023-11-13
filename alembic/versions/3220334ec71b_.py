"""empty message

Revision ID: 3220334ec71b
Revises: 00b4614e7e9a
Create Date: 2023-11-12 21:47:58.362248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3220334ec71b'
down_revision: Union[str, None] = '00b4614e7e9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
