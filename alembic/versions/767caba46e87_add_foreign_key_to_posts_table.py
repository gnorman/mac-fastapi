"""add foreign-key to posts table

Revision ID: 767caba46e87
Revises: 94e1bb280ba9
Create Date: 2023-07-09 10:15:38.365150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '767caba46e87'
down_revision = '94e1bb280ba9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
