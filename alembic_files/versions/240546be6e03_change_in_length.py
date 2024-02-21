"""change in length

Revision ID: 240546be6e03
Revises: c8401cca5d19
Create Date: 2024-02-21 15:03:10.116258

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '240546be6e03'
down_revision: Union[str, None] = 'c8401cca5d19'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
