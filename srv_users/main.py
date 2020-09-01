import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import (sessionmaker, Session)
from sqlalchemy import create_engine, MetaData
from sqlalchemy.sql import select, insert


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


Base = automap_base()
engine = create_engine("sqlite:///data/users.db?check_same_thread=False", echo=True)
Base.prepare(engine, reflect=True)

Role = Base.classes.roles

session_factory = sessionmaker(bind=engine)
session = session_factory()
query = session.query(Role).filter_by(name='administrator').all()

# m = query.all()
# mydict = to_dict(query)
#
# for k, v in mydict.items():
#     print(k, v)
# print("==========")

# engine = create_engine("sqlite:///data/users.db", echo=True)
# metadata = MetaData(bind=engine)
# metadata.reflect(bind=engine)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# SessionLocal.configure(bind=engine)
# Base = automap_base()
#
# Base.prepare(engine, reflect=True)
#
# db = SessionLocal ()
#
# db


app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'])


# Role = Base.classes.roles
# State = Base.classes.states
# User = Base.classes.users
# PaymentCard = Base.classes.payment_cards
#
# session = Session(engine)
#
# r1 = session.query(Role)


@app.get("/api/roles")
def get_roles():
    # return "Hello world"
    return session.query(Role).all()


@app.get("/api/")
def get_hello_world():
    return "Hello world"


@app.post("/api/")
def post_hello_world():
    return "Hello world"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
