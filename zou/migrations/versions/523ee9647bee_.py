"""empty message

Revision ID: 523ee9647bee
Revises: c81f3e83bdb5
Create Date: 2019-05-29 20:14:17.200661

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "523ee9647bee"
down_revision = "c81f3e83bdb5"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "comment",
        sa.Column(
            "checklist", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
    )
    op.add_column("comment", sa.Column("pinned", sa.Boolean(), nullable=True))
    op.alter_column(
        "entity",
        "description",
        existing_type=sa.VARCHAR(length=600),
        type_=sa.String(length=1200),
        existing_nullable=True,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "entity",
        "description",
        existing_type=sa.String(length=1200),
        type_=sa.VARCHAR(length=600),
        existing_nullable=True,
    )
    op.drop_column("comment", "pinned")
    op.drop_column("comment", "checklist")
    # ### end Alembic commands ###
