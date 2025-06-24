from aiohttp import ClientSession
from dotenv import load_dotenv
import os
from fastapi.encoders import jsonable_encoder

load_dotenv()
url = f"http://api.openweathermap.org/data/2.5/weather?q=санкт-петербург&lang=ru&units=metric&appid={os.getenv("WEATHER_TOKEN")}"

async def get_weather():
    async with ClientSession() as session:
        async with session.get(url=url) as response:
            return await response.json()