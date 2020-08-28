"""add products_db

Revision ID: c715b5c755b3
Revises: 
Create Date: 2020-08-28 14:26:24.458391

"""
from alembic import op
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, Float
import uuid


# revision identifiers, used by Alembic.
revision = 'c715b5c755b3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'vendors',
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False),
        Column('is_disabled', DateTime),
        Column('added_on', DateTime, default=func.now())
    )

    op.create_table(
        'products',
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False),
        Column('uuid', String, default=uuid.uuid4()),
        Column('vendor_id', Integer, ForeignKey('vendors.id')),
        Column('added_on', DateTime, default=func.now()),
        Column('is_disabled', DateTime)
    )

    op.create_table(
        'prices',
        Column('id', Integer, primary_key=True),
        Column('price', Float, nullable=False),
        Column('product_id', Integer, ForeignKey('products.id')),
        Column('added_on', DateTime, default=func.now())
    )

    op.create_table(
        'inventory',
        Column('id', Integer, primary_key=True),
        Column('count', Integer, nullable=False),
        Column('product_id', Integer, ForeignKey('products.id')),
        Column('added_on', DateTime, default=func.now())
    )


def downgrade():
    op.drop_table('inventory')
    op.drop_table('prices')
    op.drop_table('products')
    op.drop_table('vendors')
