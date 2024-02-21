from typing import List
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped , mapped_column, relationship
from sqlalchemy import Column, ForeignKey, Integer, String

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user_account'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name : Mapped[str] = mapped_column(String(50), nullable=False)
    last_name : Mapped[str] = mapped_column(String(50), nullable=False)
    username : Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    notes : Mapped[List["Note"]] = relationship("Note",back_populates="user", cascade="all, delete")


class Note(Base):
    __tablename__ = 'note'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(nullable=False)
    user: Mapped["User"] = relationship("User",back_populates="notes")
    user_id: Mapped[int] = mapped_column(ForeignKey('user_account.id'))