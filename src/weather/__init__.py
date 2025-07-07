from fastapi import APIRouter
from src.weather.weather import get_weather

router = APIRouter(tags=["weather"])

@router.get("/")
async def get_actual_weather():
    return await get_weather()