"""Renaming students to scholars

Revision ID: fffd8146e16f
Revises: 8908b5303cf1
Create Date: 2025-12-30 11:18:18.381822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fffd8146e16f'
down_revision = '8908b5303cf1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    inspector = sa.inspect(op.get_bind())
    if 'students' in inspector.get_table_names():
        op.rename_table('students', 'scholars')


def downgrade() -> None:
    inspector = sa.inspect(op.get_bind())
    if 'scholars' in inspector.get_table_names():
        op.rename_table('scholars', 'students')
