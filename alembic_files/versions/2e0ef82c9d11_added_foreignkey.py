"""added foreignkey

Revision ID: 2e0ef82c9d11
Revises: b867e38a974b
Create Date: 2024-02-21 17:26:39.798245

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e0ef82c9d11'
down_revision: Union[str, None] = 'b867e38a974b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('note', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'note', 'user_account', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'note', type_='foreignkey')
    op.drop_column('note', 'user_id')
    # ### end Alembic commands ###