"""Change blacklist to deny

Revision ID: 205742d3b3f5
Revises: 4b6587b98b26
Create Date: 2020-07-04 19:29:40.607069

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '205742d3b3f5'
down_revision = '4b6587b98b26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('key', 'blacklisted', new_column_name='denied')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('key', 'denied', new_column_name='blacklisted')
    # ### end Alembic commands ###
