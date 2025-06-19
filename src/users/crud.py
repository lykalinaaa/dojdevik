from sqlalchemy import select, delete
from src.users.schemas import UserCreate, User
from src.users.models import UserModel
from src.database import SessionDep

async def create_user(session: SessionDep,
                      user_in: UserCreate) -> UserCreate:
    user = UserModel(
        username = user_in.username,
        password = user_in.password,
        email = user_in.email,
        reg_date = user_in.reg_date
    )
    session.add(user)
    await session.commit()
    return user_in
