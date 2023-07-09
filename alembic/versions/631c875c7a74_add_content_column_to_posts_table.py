"""add content column to posts table

Revision ID: 631c875c7a74
Revises: 775c72d6c18d
Create Date: 2023-07-05 10:52:57.119167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '631c875c7a74'
down_revision = '775c72d6c18d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
