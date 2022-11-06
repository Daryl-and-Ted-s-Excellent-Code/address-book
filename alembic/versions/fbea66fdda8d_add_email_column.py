"""add email column

Revision ID: fbea66fdda8d
Revises: 
Create Date: 2022-11-05 17:48:11.887216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbea66fdda8d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('person', sa.Column('email', sa.String))
    op.create_index('ix_person_email', 'person', ['email'], unique=True)

def downgrade():
    op.drop_index('ix_person_email', 'person')
    op.drop_column('person', 'email')
