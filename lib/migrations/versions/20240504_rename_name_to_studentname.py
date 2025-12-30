"""Rename column name -> studentname on Student table."""
from alembic import op
import sqlalchemy as sa

revision = "20240504_rename_name_to_studentname"
down_revision = "fffd8146e16f"
branch_labels = None
depends_on = None

def _rename_column_if_exists(table: str, old: str, new: str) -> None:
    inspector = sa.inspect(op.get_bind())
    if table in inspector.get_table_names():
        cols = {c["name"] for c in inspector.get_columns(table)}
        if old in cols:
            op.alter_column(table, old, new_column_name=new)

def upgrade() -> None:
    _rename_column_if_exists("students", "name", "studentname")
    _rename_column_if_exists("scholars", "name", "studentname")

def downgrade() -> None:
    _rename_column_if_exists("students", "studentname", "name")
    _rename_column_if_exists("scholars", "studentname", "name")
