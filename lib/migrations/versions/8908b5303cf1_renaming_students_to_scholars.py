"""Renaming students to scholars

Revision ID: 8908b5303cf1
Revises: 791279dd0760
Create Date: 2025-12-30 11:12:53.710068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8908b5303cf1'
down_revision = '791279dd0760'
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
