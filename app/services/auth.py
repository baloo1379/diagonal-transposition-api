from fastapi import Depends, status, HTTPException
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from os import getenv

from app.database.connection import get_db
from app.repositories.user_repository import get_user_by_username
from app.schemas.user import User

SECRET_KEY = getenv('SECRET_KEY', 'not_so_secret')
ALGORITHM = getenv('ALGORITHM', 'HS256')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBasic()


def abort_authentication():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Basic"},
    )


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db: Session, username: str) -> User:
    user = get_user_by_username(db, username)
    if not user:
        return abort_authentication()
    return User(**user.as_dict())


def authenticate_user(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)) -> User:
    user = get_user(db, credentials.username)
    if not verify_password(credentials.password, user.password):
        return abort_authentication()
    return user
