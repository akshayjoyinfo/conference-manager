"""Change the data type

Revision ID: 653be5ceec5f
Revises: 27ce91b58a43
Create Date: 2021-09-03 10:48:59.946030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '653be5ceec5f'
down_revision = '27ce91b58a43'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('ALTER TABLE talks ALTER COLUMN duration TYPE VARCHAR')


def downgrade():
    pass
