"""updated Talk users tables

Revision ID: 0cdd76af62e8
Revises: 653be5ceec5f
Create Date: 2021-09-04 22:52:59.034094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cdd76af62e8'
down_revision = '653be5ceec5f'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""ALTER TABLE participants ADD COLUMN conference_id INT NOT NULL
                CONSTRAINT participant_conference REFERENCES conferences (id) ON UPDATE CASCADE ON DELETE CASCADE; """)
    
    op.execute("""ALTER TABLE speakers ADD COLUMN conference_id INT NOT NULL
                CONSTRAINT speaker_conference REFERENCES conferences (id) ON UPDATE CASCADE ON DELETE CASCADE; """)


def downgrade():
    pass
