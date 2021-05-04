from sqlalchemy.exc import IntegrityError
import warnings

from sqlalchemy.orm import Session

from app.models.user import User as UserEntity, Base
from app.repositories.user_repository import save_user
from app.database.connection import SessionLocal, engine
from app.services.auth import get_password_hash
from os import getenv


def seeder(db: Session = SessionLocal()):
    try:
        Base.metadata.create_all(bind=engine)
        save_user(db, UserEntity(username=getenv('DEFAULT_USER', 'diagonal'),
                                 password=get_password_hash(getenv('DEFAULT_PASSWORD', 'transposition'))))
    except IntegrityError as er:
        warnings.warn(er.orig)


if __name__ == '__main__':
    seeder()
