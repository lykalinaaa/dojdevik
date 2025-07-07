from fastapi import APIRouter, HTTPException, status, Request, Depends
from src.users.crud import create_user
from src.database import SessionDep
from src.users.schemas import UserCreate, User

router = APIRouter(tags=["users"])

@router.post("/create_user", response_model=UserCreate)
async def create_new_book(session: SessionDep, user_in: UserCreate):
    return await create_user(session, user_in)