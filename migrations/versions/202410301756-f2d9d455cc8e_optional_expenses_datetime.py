"""Optional expenses.datetime and expenses.description

Revision ID: f2d9d455cc8e
Revises: 2ca0c7119d91
Create Date: 2024-10-30 17:56:44.430258

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "f2d9d455cc8e"
down_revision: Union[str, None] = "2ca0c7119d91"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("expenses_expenses", "description", existing_type=sa.VARCHAR(), nullable=True)
    op.alter_column("expenses_expenses", "datetime", existing_type=postgresql.TIMESTAMP(), nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("expenses_expenses", "datetime", existing_type=postgresql.TIMESTAMP(), nullable=False)
    op.alter_column("expenses_expenses", "description", existing_type=sa.VARCHAR(), nullable=False)
    # ### end Alembic commands ###
