from sqlalchemy import Column, Integer, String

from database.connection import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    def as_dict(self):
        return {"id": self.id, "username": self.username, "password": self.password}


