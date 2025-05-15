
from sqlalchemy.orm import  Mapped, mapped_column
from sqlalchemy import String
from typing import Optional
from db import  Base


class UserProfile(Base):
    email: Mapped[str] = mapped_column(unique=True)
    name: Mapped[Optional[str]] = mapped_column(String(50))
    password: Mapped[str]