import os

from alembic import op
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, Float, orm, PrimaryKeyConstraint
from sqlalchemy.sql import insert
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from werkzeug.security import generate_password_hash, check_password_hash

Session = sessionmaker()
Base = declarative_base()


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True),
    name = Column(String, nullable=False)

    PrimaryKeyConstraint('id')


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True),
    name = Column(String, nullable=False),
    abbrev = Column(String, nullable=False),
    tax_rate = Column(Float, nullable=False)

    PrimaryKeyConstraint('id')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    password_hash = Column(String, nullable=False)
    uuid = Column(String, default=uuid.uuid4())
    name = Column(String, nullable=False)
    address1 = Column(String, nullable=False)
    address2 = Column(String)
    city = Column(String, nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'))
    zip = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    added_on = Column(DateTime, default=func.now())
    is_employee_account = Column(DateTime)
    is_disabled_account = Column(DateTime)

    PrimaryKeyConstraint('id')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class PaymentCard(Base):
    __tablename__ = 'payment_cards'
    id = Column(Integer, primary_key=True)
    account = Column(Integer, nullable=False)
    ccv = Column(Integer, nullable=False)
    expiration = Column(DateTime, nullable=False)
    added_on = Column(DateTime, default=func.now())
    is_disabled_account = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))

    PrimaryKeyConstraint('id')

