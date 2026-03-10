from pydantic import BaseModel, Field, EmailStr, ValidationError

class UserRegister(BaseModel):
   
    username: str = Field(..., min_length=5)
    
    email: EmailStr
    
    
    age: int = Field(..., ge=18)

def register_user(data):
    try:
        user = UserRegister(**data)
        print(" Validation Successful!")
        print(user)
    except ValidationError as e:
        print("Validation Failed:")
        print(e.json())

register_user({"username": "tanvir", "email": "sktanvir@gmail.com", "age": 25})
