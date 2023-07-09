"""create posts table

Revision ID: 775c72d6c18d
Revises: 
Create Date: 2023-07-05 10:51:13.078673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '775c72d6c18d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass

def downgrade():
    op.drop_table('posts')
    pass
