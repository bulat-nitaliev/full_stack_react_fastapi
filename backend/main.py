from fastapi import FastAPI
from users import  user_router, auth_router

from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost:3000/",
    "http://10.64.0.86:3000/",
    "http://10.64.0.86:8000/",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
]




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router)
app.include_router(auth_router)