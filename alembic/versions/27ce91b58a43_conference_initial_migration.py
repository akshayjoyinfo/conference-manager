"""Conference Initial migration

Revision ID: 27ce91b58a43
Revises: 
Create Date: 2021-09-03 00:44:38.721414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27ce91b58a43'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'conferences',
        sa.Column('id', sa.Integer,primary_key=True),
        sa.Column('title', sa.String(length=250)),
        sa.Column('description', sa.String(10000)),
        sa.Column('start_date', sa.DateTime),
        sa.Column('end_date', sa.DateTime),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime)
    )

    op.create_table(
        'talks',
        sa.Column('id', sa.Integer,primary_key=True),
        sa.Column('title', sa.String(length=250)),
        sa.Column('description', sa.String(10000)),
        sa.Column('talk_date', sa.DateTime),
        sa.Column('duration', sa.Time),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
        sa.Column('conference_id', sa.Integer),
    )

    op.create_table(
        'profiles',
        sa.Column('id', sa.Integer,primary_key=True),
        sa.Column('username', sa.String(length=50)),
        sa.Column('email', sa.String(50)),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime)
    )

    op.create_table(
        'participants',
        sa.Column('id', sa.Integer,primary_key=True),
        sa.Column('profile_id', sa.Integer),
        sa.Column('talk_id', sa.Integer)
    )

    op.create_table(
        'speakers',
        sa.Column('id', sa.Integer,primary_key=True),
        sa.Column('profile_id', sa.Integer),
        sa.Column('talk_id', sa.Integer)
    )



def downgrade():
    op.drop_table('profiles')
    op.drop_table('speakers')
    op.drop_table('participants')
    op.drop_table('talks')
    op.drop_table('conferences')

