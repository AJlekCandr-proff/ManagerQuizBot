"""Tiny fixs

Revision ID: 84b2b9ee7ccd
Revises: ba2ecd4cf808
Create Date: 2024-11-28 16:07:14.623672

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84b2b9ee7ccd'
down_revision: Union[str, None] = 'ba2ecd4cf808'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('correct_answer', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'correct_answer')
    # ### end Alembic commands ###