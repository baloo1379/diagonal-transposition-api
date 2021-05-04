from sqlalchemy.orm import Session

from app.models.user import User as UserEntity
from app.schemas.user import UserCreate


def get_user_by_username(db: Session, username: str) -> UserEntity:
    return db.query(UserEntity).filter(UserEntity.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(UserEntity).offset(skip).limit(limit).all()


def save_user(db: Session, user: UserCreate) -> UserEntity:
    db_user = UserEntity(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
