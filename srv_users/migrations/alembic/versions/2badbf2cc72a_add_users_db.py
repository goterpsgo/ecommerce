"""add users_db

Revision ID: 2badbf2cc72a
Revises: 
Create Date: 2020-08-28 13:39:27.472806

"""
from alembic import op
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
import uuid


# revision identifiers, used by Alembic.
revision = '2badbf2cc72a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'states',
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False),
        Column('tax_rate', Integer, nullable=False),
        Column('abbreviation', String)
    )

    op.create_table(
        'users',
        Column('id', Integer, primary_key=True),
        Column('password_hash', String),
        Column('uuid', String, default=uuid.uuid4()),
        Column('name', String),
        Column('address1', String),
        Column('address2', String),
        Column('city', String),
        Column('state_id', Integer, ForeignKey('states.id')),
        Column('zip', Integer),
        Column('added_on', DateTime, default=func.now()),
        Column('is_employee_account', DateTime),
        Column('is_disabled_account', DateTime)
    )

    op.create_table(
        'payment_cards',
        Column('id', Integer, primary_key=True),
        Column('account', Integer),
        Column('ccv', Integer),
        Column('expiration', DateTime),
        Column('added_on', DateTime, default=func.now()),
        Column('is_disabled_account', DateTime),
        Column('user_id', Integer, ForeignKey('users.id'))
    )


def downgrade():
    op.drop_table('payment_cards')
    op.drop_table('user')
    op.drop_table('state')
