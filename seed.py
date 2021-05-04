from models.user import User as UserEntity
from repositories.user_repository import save_user
from database.connection import SessionLocal
from os import getenv


def seeder():
    db = SessionLocal()
    # user: diagonal
    # password: transposition
    save_user(db, UserEntity(username=getenv('DEFAULT_USER', 'diagonal'),
                             password=getenv('DEFAULT_PASSWORD', '$2b$12$DXIbNRKF/Re589NIGF7SBO8Nxzg1s1tRrK4MuOUQD0VSXicdsO95G')))


if __name__ == '__main__':
    seeder()
