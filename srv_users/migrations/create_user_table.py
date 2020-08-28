import os

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash


Base = declarative_base()

class State(Base):
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    abbreviation = Column(String)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    password_hash = Column(String)
    uuid = Column(String)
    name = Column(String)
    address1 = Column(String)
    address2 = Column(String)
    city = Column(String)
    state_id = Column(Integer, ForeignKey('state.id'))
    zip = Column(Integer)
    added_on = Column(DateTime, default=func.now())
    is_employee_account = Column(DateTime)
    is_disabled_account = Column(DateTime)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class PaymentCards(Base):
    __tablename__ = 'payment_cards'
    id = Column(Integer, primary_key=True)
    account = Column(Integer)
    ccv = Column(Integer)
    expiration = Column(DateTime)
    added_on = Column(DateTime, default=func.now())
    is_disabled_account = Column(DateTime)

# pwhash = bcrypt.hashpw(login_data['password'], user.password)
# if user.password == pwhash:
#     print
#     'Access granted'

db_name = '../data/users.db'
if os.path.exists(db_name):
    os.remove(db_name)

from sqlalchemy import create_engine

engine = create_engine('sqlite:///' + db_name)

from sqlalchemy.orm import sessionmaker

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
