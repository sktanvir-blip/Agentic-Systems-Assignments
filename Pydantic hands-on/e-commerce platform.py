from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Address(BaseModel):
    city: str = Field(min_length=3)
    
    pincode: str = Field(pattern=r"^\d{6}$")

class User(BaseModel):
    user_id: int
    name: str
    
    email: EmailStr
    
    age: int = Field(ge=18) 
    
    address: Address
    
    is_premium: Optional[bool] = False

    model_config = {
        "validate_assignment": True
    }

try:
    my_address = Address(city="Mumbai", pincode="123456")
    
    new_user = User(
        user_id=1,
        name="Tanvir Shaikh",
        email="tanvir@gmail.com",
        age=25,
        address=my_address
    )
    
    print(f"Success! User created: {new_user.name}")
    
except Exception as e:
    print(f"Error found: {e}")