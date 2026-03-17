from pydantic import BaseModel, Field, EmailStr, ValidationError
from typing import Optional

class Adress(BaseModel):
    city: str =Field(min_length=3)
    pincode: str = Field(pattern=r"^\d{6}$")

class User(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    age: int = Field(ge=18)
    address: Adress
    is_premium: Optional[bool] = False

    model_config ={
        "validate assignment":True
    }
try:
    My_Adress=Adress(city="Nashik", pincode="423206")
    NewUser = User(
        user_id=9834,
        name="Tanvir",
        email="tanvir@gmail.com",
        age=25,
        address=My_Adress
    )
except ValidationError as e:
    print(f"Error found: {e}")