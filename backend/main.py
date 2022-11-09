from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserAuthRequest(BaseModel):
    username: str
    password: str

class UserAuthResponse(BaseModel):
    status: str

fakedata = [
    {
        'username': 'admin',
        'password': 'admin123'
    },
    {
        'username': 'user',
        'password': 'user123'
    },
    {
        'username': 'guest',
        'password': 'guest123'
    },
]

@app.get('/')
def index():
    return {'Server Status': 'Server OK'}

@app.post('/auth', response_model=UserAuthResponse)
def login(userinfo: UserAuthRequest):
    for user in fakedata:
        if user['username'] == userinfo.username:
            if user['password'] == userinfo.password:
                return UserAuthResponse(
                    status= "User Successfully Login!"
                )
            return UserAuthResponse(
                    status= "Password Incorrect!"
                )
    return UserAuthResponse(
        status= "User Not Found!"
    )