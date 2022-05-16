"""create all table

Revision ID: 598f53510d33
Revises: 
Create Date: 2022-05-16 09:56:10.799555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '598f53510d33'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    CREATE TABLE users(
     id =
    )
    pass


def downgrade():
    pass
