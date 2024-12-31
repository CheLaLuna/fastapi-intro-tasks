from fastapi import FastAPI, Body
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# BEGIN (write your solution here)
class User(BaseModel):
    username: str
    email: str
    age: Optional[int] = None

@app.post("/users")
async def create_user(user: User):
    return {
        "username": user.username,
        "email": user.email,
        "age": user.age,
        "status": "User created"
    }
# END
