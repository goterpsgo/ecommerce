"""add carts_db

Revision ID: b9e976344f75
Revises: 
Create Date: 2020-08-28 13:36:36.457247

"""
from alembic import op
from sqlalchemy import Column, DateTime, String, Integer, func


# revision identifiers, used by Alembic.
revision = 'b9e976344f75'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'carts',
        Column('id', Integer, primary_key=True),
        Column('user_uuid', String),
        Column('added_on', DateTime, default=func.now())
    )

    op.create_table(
        'items',
        Column('id', Integer, primary_key=True),
        Column('product_uuid', String, nullable=False),
        Column('count', Integer),
        Column('added_on', DateTime, default=func.now())
    )


def downgrade():
    op.drop_table('items')
    op.drop_table('carts')
