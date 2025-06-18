from datetime import datetime
from pydantic import EmailStr
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base

class UserModel(Base):
    username: Mapped[str] = mapped_column(
        String(lenght=14),
        unique=True,
        nullable=False
    )
    password: Mapped[str] = mapped_column(
        nullable=False
    )
    email: Mapped[EmailStr] = mapped_column(
        unique=True,
        nullable=False
    )
    reg_date: Mapped[datetime] = mapped_column(
        default=datetime.now
    )