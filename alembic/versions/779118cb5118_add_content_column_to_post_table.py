"""add content column to post table

Revision ID: 779118cb5118
Revises: eed2082e6069
Create Date: 2022-05-27 19:17:21.000630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '779118cb5118'
down_revision = 'eed2082e6069'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
