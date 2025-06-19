from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr

class UserBase(BaseModel):
    username: str
    password: str
    email: EmailStr
    reg_date: datetime = datetime.now().isoformat(timespec='seconds')

class UserCreate(UserBase):
    pass

class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int