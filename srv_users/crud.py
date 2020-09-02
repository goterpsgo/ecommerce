from sqlalchemy.orm import Session

from . import models, schemas


def get_roles(db: Session):
    return db.query(models.Role).all()
