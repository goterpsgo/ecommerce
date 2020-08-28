"""add transactions_db

Revision ID: 10c9f19f38e7
Revises: 
Create Date: 2020-08-28 16:10:38.805920

"""
from alembic import op
from sqlalchemy import Column, DateTime, String, Integer, func, Float


# revision identifiers, used by Alembic.
revision = '10c9f19f38e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'transactions',
        Column('id', Integer, primary_key=True),
        Column('cart_uuid', String),
        Column('price', Float),
        Column('added_on', DateTime, default=func.now())
    )


def downgrade():
    op.drop_table('transactions')
