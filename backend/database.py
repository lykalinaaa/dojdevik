from fastapi import Depends
from sqlalchemy import Integer
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from dotenv import load_dotenv
import os
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from typing import Annotated

load_dotenv()
async_engine = create_async_engine(
    url=os.getenv("DATABASE_URL")
)

new_session = async_sessionmaker(bind=async_engine)

async def create_session():
    async with new_session() as session:
        yield session


SessionDep = Annotated[
    AsyncSession,
    Depends(create_session)
]

class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"