"""add users_db

Revision ID: 2badbf2cc72a
Revises: 
Create Date: 2020-08-28 13:39:27.472806

"""
from alembic import op
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, Float
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import datetime


# revision identifiers, used by Alembic.
revision = '2badbf2cc72a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'roles',
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False)
    )

    op.execute("INSERT INTO roles (name)"
               "VALUES ('administrator'), ('editor'), ('employee'), ('customer')")

    op.create_table(
        'states',
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False),
        Column('tax_rate', Float, nullable=False),
        Column('abbreviation', String)
    )

    op.execute("INSERT INTO states (name, tax_rate, abbreviation)"
               "VALUES ('Maryland', 6.0, 'MD'),"
               "('Virginia', 6.0, 'VA'),"
               "('District of Columbia', 6.0, 'DC')")

    op.create_table(
        'users',
        Column('id', Integer, primary_key=True),
        Column('password_hash', String, nullable=False),
        Column('uuid', String, default=uuid.uuid4()),
        Column('first_name', String, nullable=False),
        Column('last_name', String, nullable=False),
        Column('address1', String, nullable=False),
        Column('address2', String),
        Column('city', String, nullable=False),
        Column('state_id', Integer, ForeignKey('states.id')),
        Column('zip', Integer, nullable=False),
        Column('role_id', Integer, ForeignKey('roles.id')),
        Column('added_on', DateTime, default=func.now()),
        Column('is_employee_account', DateTime),
        Column('is_disabled_account', DateTime)
    )

    op.execute(
        "INSERT INTO users (password_hash, uuid, first_name, last_name, address1, city, state_id, zip, "
        "role_id, added_on, is_employee_account) "
        " VALUES "
        "("
            "'" + generate_password_hash("password") + "',"
            "'" + str(uuid.uuid4()) + "', 'Admin', 'User', '1600 Pennsylvania Ave',"
            "'Washington',"
            "(select (id) from states where abbreviation = 'DC'),"
            "20001,"
            "(select (id) from roles where name = 'administrator'),"
            "datetime('now', 'localtime'),"
            "datetime('now', 'localtime')"
        ")"
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
    op.drop_table('users')
    op.drop_table('state')
    op.drop_table('roles')
