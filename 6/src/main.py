from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/login", response_class=HTMLResponse)
async def get_login_form():
    return """
    <form action="/login" method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
    """

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    return {
        "username": username,
        "password": password,
        "status": "Login successful"
    }
# END
