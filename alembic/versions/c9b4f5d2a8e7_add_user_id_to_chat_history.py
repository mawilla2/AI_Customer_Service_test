"""add user id to chat history

Revision ID: c9b4f5d2a8e7
Revises: 7f33d1d8c6c1
Create Date: 2026-05-27 21:20:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "c9b4f5d2a8e7"
down_revision: Union[str, Sequence[str], None] = "7f33d1d8c6c1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "chat_history",
        sa.Column("user_id", sa.Integer(), nullable=True),
    )
    op.create_foreign_key(
        "fk_chat_history_user_id_users",
        "chat_history",
        "users",
        ["user_id"],
        ["id"],
    )


def downgrade() -> None:
    op.drop_constraint(
        "fk_chat_history_user_id_users",
        "chat_history",
        type_="foreignkey",
    )
    op.drop_column("chat_history", "user_id")
